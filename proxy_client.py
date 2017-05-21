# -*- coding: utf-8 -*-

from __future__ import absolute_import
import logging
import socket

import thriftpy
from thrift_connector import ClientPool, ThriftPyCyClient

from spider import setting

proxy_thrift = thriftpy.load("resource/proxy.thrift", module_name="proxy_thrift")

logger = logging.getLogger(__name__)

class ProxyClient(object):
    """代理服务客户端简单封装"""
    proxy = ClientPool(
        proxy_thrift.ProxyService,
        setting.PROXY_SERVICE_HOST,
        setting.PROXY_SERVICE_PORT,
        connection_class=ThriftPyCyClient
    )

    @classmethod
    def get_proxy(cls, url):
        """
        获取代理
        :param url: 请求的url地址，需要根据schema和host返回一个合适的代理
        :return: 
        """
        req = proxy_thrift.ProxyReq()
        req.url = url
        try:
            response = cls.proxy.get_proxy(req)
            return response
        except Exception as e:
            logging.exception(e)
            return None


if __name__ == "__main__":
    ProxyClient.get_proxy("www.didichuxing.com")