import Pyro4

# Define the remote interface
@Pyro4.expose
class StringConcatServer(object):
    def concatenate(self, s1, s2):
        return s1 + s2

# Register the server object with Pyro4
daemon = Pyro4.Daemon()
uri = daemon.register(StringConcatServer)

# Make the server available for remote calls under the name "ConcatService"
with Pyro4.locateNS() as ns:
    ns.register("ConcatService", uri)

print("Service is bound and ready for use...")

# Start the Pyro4 event loop
daemon.requestLoop()
