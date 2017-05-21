# -*- coding: utf-8 -*-

from multiprocessing import cpu_count

worker_class = "thriftpy_gevent"
thrift_protocol_factory = "thriftpy.protocol:TBinaryProtocolFactory"
thrift_transport_factory = "thriftpy.transport:TBufferedTransportFactory"

workers = cpu_count()

errorlog = "-"
loglevel = "info"
