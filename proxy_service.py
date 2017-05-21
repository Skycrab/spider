# -*- coding: utf-8 -*-

from __future__ import absolute_import

import thriftpy
from thriftpy.rpc import make_server
from thrift_connector import ClientPool, ThriftPyCyClient

from spider import setting

proxy_thrift = thriftpy.load("resource/proxy.thrift", module_name="proxy_thrift")

class ProxyDispatcher(object):
    def get_proxy(self, proxyReq):
        proxy = proxy_thrift.Proxy()
        proxy.url = "http://www.google.com"
        # e = proxy_thrift.ExceptionError(1, "error")
        # raise e
        return proxy


def main():
    '''普通运行模式 '''
    server = make_server(proxy_thrift.ProxyService, ProxyDispatcher(),
                         '127.0.0.1', 6000)
    print("serving...")
    server.serve()

if __name__ == "__main__":
    main()
