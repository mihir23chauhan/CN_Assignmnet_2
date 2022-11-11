from mininet.topo import Topo
from mininet.link import TCLink


class MyTopo(Topo):

    def build(self):

        # Adding Hosts
        aHost = self.addHost('hA')
        bHost = self.addHost('hB')
        cHost = self.addHost('hC')
        dHost = self.addHost('hD')

        # Adding switches
        rOneSwitch = self.addSwitch('r1')
        rTwoSwitch = self.addSwitch('r2')

        # Add links
        self.addLink(aHost, rOneSwitch, cls=TCLink, bw=1000, delay='1ms')
        self.addLink(dHost, rOneSwitch, cls=TCLink, bw=1000, delay='1ms')
        self.addLink(bHost, rTwoSwitch, cls=TCLink, bw=1000, delay='1ms')
        self.addLink(cHost, rTwoSwitch, cls=TCLink, bw=1000, delay='1ms')
        self.addLink(rOneSwitch, rTwoSwitch, cls=TCLink, bw=500, delay='10ms')


topos = {'mytopo': (lambda: MyTopo())}
