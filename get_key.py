#!/usr/bin/python
# coding: utf-8


from ConfigParser import ConfigParser
import redis, os

rds = redis.StrictRedis(host='localhost', port=6379)


def init_data(xs, Flag=1):
    service_data = {}
    if Flag == 1:
        os.system('redis-cli flushall')
        for service in xs:
            service_data[service] = []
            config = ConfigParser()
            cfg = os.path.join(os.path.join(os.getcwd(), 'conf'), service)
            config.read(cfg)
            session = config.sections()
            for index in range(len(session)):
                jiekou = session[index]
                service_data[service].append(jiekou)
                rds.set(service + ':' + jiekou + ':url', config.get(jiekou, 'url'))
                rds.set(service + ':' + jiekou + ':keywords', config.get(jiekou, 'keywords'))
                rds.set(service + ':' + jiekou + ':status', '00000')
                rds.set(service + ':' + jiekou + ':sendflag', 1)
    return service_data
