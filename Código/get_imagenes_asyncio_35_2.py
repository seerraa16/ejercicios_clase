#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from os import sep
from sys import stderr

import asyncio

from http.client import HTTPConnection
from contextlib import closing
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from timeit import timeit


def wget(uri):
    """
    Devuelve el contenido indicado por una URI

    Parámetro:
    > uri (str, por ejemplo 'http://inspyration.org')

    Retorno:
    > contenido de un archivo (bytes, archivo de texto o binario)
    """
    # Análisis de la URI
    parsed = urlparse(uri)
    # apertura de la conexión
    with closing(HTTPConnection(parsed.netloc)) as conn:
        # Ruta en el servidor
        path = parsed.path
        if parsed.query:
            path += '?' + parsed.query
        # Envío de la consulta al servidor
        conn.request('GET', path)
        # Recuperación de la respuesta
        response = conn.getresponse()
        # Análisis de la respuesta
        if response.status != 200:
            # 200 = Ok, 3xx = redireccion, 4xx = error cliente, 5xx = error servidor
            return
        # Reenvío de la respuesta si todo está OK.
        return response.read()


async def download(uri):
    """
    Guarda en el disco duro un archivo indicado por una URI

    Parámetro:
    > uri (str, por ejemplo 'http://www.inspyration.org/logo.png')

    Retorno:
    > contenido de un archivo (bytes, archivo de texto o binario)
    """
    content = wget(uri)
    if content is None:
        return None
    async with open(uri.split(sep)[-1], 'wb') as f:
        await f.write(content)
        return uri


class ImageFinderAwaitable:
    def __init__(self, html_doc):
        self.html_doc = html_doc

    async def __await__(self):
        self.soup = BeautifulSoup(self.html_doc, "html.parser")
        return self.soup.find_all('img')


class ImageFinder:
    def __init__(self, html_doc):
        self.html_doc = html_doc

    async def __aiter__(self):
        return self

    async def __anext__(self):
        for img in ImageFinderAwaitable(self.html_doc):
            await img.get('src')


class URIRetreiver:
    def __init__(self, base_uri, image_finder):
        self.parsed_base = urlparse(base_uri)
        self.image_finder = image_finder

    async def __aiter__(self):
        return self

    async def __anext__(self):
        async for src in self.image_finder:
            parsed = urlparse(src)
            if parsed.netloc == '':
                path = parsed.path
                if parsed.query:
                    path += '?' + parsed.query
                if path[0] != '/':
                    if self.parsed_base.path == '/':
                        path = '/' + path
                    else:
                        path = '/' + '/'.join(self.parsed_base.path.split('/')[:-1]) + '/' + path
                await self.parsed_base.scheme + '://' + self.parsed_base.netloc + path
            else:
                await parsed.geturl()


def get_images_uri(page_uri):
    #
    # Recuperación de las URI de todas las imágenes de una página
    #
    html = wget(page_uri)
    if not html:
        print("Error: La página web no se ha encontrado o analizado", sys.stderr)
        return None
    images_src_coroutine = ImageFinder(html)
    images_uri_coroutine = URIRetreiver(page_uri, images_src_coroutine)


    return images_uri_coroutine


async def parse_html_page_and_get_all_images(page_uri):
    images_uri = get_images_uri('http://www.formation-python.com/')
    #
    # Recuperación de las imágenes
    #
    async for image_uri in images_uri:
        print('Descarga de %s' % image_uri)
        await download(image_uri)


def do(page_uri):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(parse_html_page_and_get_all_images(page_uri))
    loop.close()


if __name__ == '__main__':
    print('--- Starting standard download ---')
    web_page_uri = 'http://www.formation-python.com/'
    print(timeit('do(web_page_uri)',
                 number=10,
                 setup="from __main__ import do, web_page_uri"))

# Tiempo evaluado: 4.63s

