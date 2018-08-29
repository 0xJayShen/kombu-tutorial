# -*- coding: utf8 -*-
import gevent.monkey
gevent.monkey.patch_all()

import gevent.lock
greenlets = {}
semaphore = gevent.lock.Semaphore(5)
def async(fn):
    def _fn(*args, **kwargs):
        fn(*args, **kwargs)
        del greenlets[id(gevent.getcurrent())]
        semaphore.release()

    def spawn_greenlet(*args, **kwargs):
        greenlet = gevent.spawn(_fn, *args, **kwargs)
        greenlets[id(greenlet)] = greenlet

    return spawn_greenlet