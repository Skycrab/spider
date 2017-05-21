# -*- coding: utf-8 -*-

from __future__ import absolute_import

import logging

import thriftpy
from thriftpy.rpc import make_server
from thriftpy.thrift import TProcessor

from spider.proxy_client import ProxyClient


logger = logging.getLogger(__name__)

task_thrift = thriftpy.load("resource/task.thrift", module_name="task_thrift")


class TaskDispatcher(object):
    @classmethod
    def success(cls):
        response = task_thrift.TaskResponse()
        response.code = 0
        response.message = "ok"
        return response

    @classmethod
    def failed(cls):
        raise task_thrift.ExceptionError(1, "异常")


    """任务处理"""
    def add_task(self, req):
        logger.info("receive task:%s", req)
        print(req)
        try:
            proxy = ProxyClient.get_proxy(req.url)
        except Exception as e:
            logger.exception(e)
            print(e)
            return self.failed()
        return self.success()


def main():
    '''普通运行模式 '''
    server = make_server(task_thrift.TaskService, TaskDispatcher(),
                         '127.0.0.1', 8000)
    print("serving...")
    server.serve()

'''
gunicorn运行模式
'''
app = TProcessor(task_thrift.TaskService, TaskDispatcher())


if __name__ == '__main__':
    main()


