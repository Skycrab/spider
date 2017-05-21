# -*- coding: utf-8 -*-

import thriftpy

from thriftpy.rpc import client_context

task_thrift = thriftpy.load("resource/task.thrift", module_name="task_thrift")

def main():
    with client_context(task_thrift.TaskService, '127.0.0.1', 8000) as c:
        task = task_thrift.TaskReq()
        task.url="www.baidu.com"
        response = c.add_task(task)
        print(response)


if __name__ == '__main__':
    main()
