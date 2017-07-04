import ssl_server

from settings import config
pconfig = config.autoprefix("PUBLIC_RELAY_")


class RequestHandler(object):
    def handle(self):
        print("ohai")

class PublicRelayServer(ssl_server.SSLServer):
    pass


def main():
    pconfig.require(
        "ACCEPT_DOMAINS",
    )
    server = PublicRelayServer(
        (pconfig.BIND_HOST, pconfig.BIND_PORT),
        RequestHandler,
        pconfig.CERT_FILE,
        pconfig.KEY_FILE,
    )
    server.serve_forever()

if __name__ == '__main__':
    main()
