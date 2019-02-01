def test_index(client):
    response = client.get("/")
    assert b"NAPALM-Inspector" in response.data


def test_test_getters(client):
    response = client.get("/test-getters/")
    assert b"ios" in response.data


def test_test_getters_platforms(client):
    response = client.get("/test-getters/ios/")
    assert b"get_facts" in response.data
    assert b"get_lldp_neighbors" in response.data


def test_404(client):
    response = client.get("/not-found/")
    assert response.status_code == 404


def test_ios_get_facts_get(client):
    response = client.get("/test-getters/ios/get_facts")
    assert b"get_facts" in response.data


arp_table = """Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  172.29.50.1             8   84b8.0276.ac0e  ARPA   Vlan20
Internet  172.29.50.2           221   0019.0725.344a  ARPA   Vlan20
Internet  172.29.50.3             -   0024.f7dd.7741  ARPA   Vlan20
Internet  172.29.50.10           37   6805.ca12.71c2  ARPA   Vlan20
Internet  172.29.52.33           61   84b8.0276.ac0e  ARPA   Vlan41
Internet  172.29.52.34            -   0024.f7dd.7743  ARPA   Vlan41
Internet  172.29.52.40            3   a099.9b1c.dfa7  ARPA   Vlan41
Internet  192.168.81.34           -   0024.f7dd.7743  ARPA   Vlan41
"""


def test_ios_get_arp_table_post(client):
    data = {"show_arp___exclude_Incomplete": arp_table}
    response = client.post("/test-getters/ios/get_arp_table", data=data)

    assert b"172.29.52.33" in response.data
    assert b"Output from get_arp_table" in response.data
    assert b"Copy and paste the output below" in response.data


def test_ios_get_arp_table_post_forced_error(client):
    broken_arp = arp_table.replace("a099.9b1c.dfa7", "Incomplete")
    data = {"show_arp___exclude_Incomplete": broken_arp}
    response = client.post("/test-getters/ios/get_arp_table", data=data)

    assert b"172.29.52.33" in response.data
    assert b"Invalid MAC Address detected" in response.data


ip_interfaces = """
IP Interface Status for VRF "default"
Ethernet2/1, Interface status: protocol-up/link-up/admin-up, iod: 37,
  IP address: 1.1.1.1, IP subnet: 1.1.1.0/24 route-preference: 0, tag: 0
  IP broadcast address: 255.255.255.255
  IP multicast groups locally joined: none
  IP MTU: 1500 bytes (using link MTU)
  IP primary address route-preference: 0, tag: 0
  IP proxy ARP : disabled
  IP Local Proxy ARP : disabled
  IP multicast routing: disabled
  IP icmp redirects: enabled
  IP directed-broadcast: disabled
  IP Forwarding: disabled
  IP icmp unreachables (except port): disabled
  IP icmp port-unreachable: enabled
  IP unicast reverse path forwarding: none
  IP load sharing: none
  IP interface statistics last reset: never
  IP interface software stats: (sent/received/forwarded/originated/consumed)
    Unicast packets    : 59/57/0/237/292
    Unicast bytes      : 4829/3619/0/15823/18232
    Multicast packets  : 0/0/0/0/0
    Multicast bytes    : 0/0/0/0/0
    Broadcast packets  : 0/0/0/0/0
    Broadcast bytes    : 0/0/0/0/0
    Labeled packets    : 0/0/0/0/0
    Labeled bytes      : 0/0/0/0/0
  WCCP Redirect outbound: disabled
  WCCP Redirect inbound: disabled
  WCCP Redirect exclude: disabled
Ethernet2/2, Interface status: protocol-up/link-up/admin-up, iod: 38,
  IP address: 2.2.2.2, IP subnet: 2.2.2.0/27 route-preference: 0, tag: 0
  IP address: 3.3.3.3, IP subnet: 3.3.3.0/25 secondary route-preference: 0, tag: 0
  IP broadcast address: 255.255.255.255
  IP multicast groups locally joined: none
  IP MTU: 1500 bytes (using link MTU)
  IP primary address route-preference: 0, tag: 0
  IP proxy ARP : disabled
  IP Local Proxy ARP : disabled
  IP multicast routing: disabled
  IP icmp redirects: disabled
  IP directed-broadcast: disabled
  IP Forwarding: disabled
  IP icmp unreachables (except port): disabled
  IP icmp port-unreachable: enabled
  IP unicast reverse path forwarding: none
  IP load sharing: none
  IP interface statistics last reset: never
  IP interface software stats: (sent/received/forwarded/originated/consumed)
    Unicast packets    : 0/0/0/0/0
    Unicast bytes      : 0/0/0/0/0
    Multicast packets  : 0/0/0/0/0
    Multicast bytes    : 0/0/0/0/0
    Broadcast packets  : 0/0/0/0/0
    Broadcast bytes    : 0/0/0/0/0
    Labeled packets    : 0/0/0/0/0
    Labeled bytes      : 0/0/0/0/0
  WCCP Redirect outbound: disabled
  WCCP Redirect inbound: disabled
  WCCP Redirect exclude: disabled
Ethernet2/3, Interface status: protocol-up/link-up/admin-up, iod: 39,
  IP address: 4.4.4.4, IP subnet: 4.4.0.0/16 route-preference: 0, tag: 0
  IP broadcast address: 255.255.255.255
  IP multicast groups locally joined: none
  IP MTU: 1500 bytes (using link MTU)
  IP primary address route-preference: 0, tag: 0
  IP proxy ARP : disabled
  IP Local Proxy ARP : disabled
  IP multicast routing: disabled
  IP icmp redirects: enabled
  IP directed-broadcast: disabled
  IP Forwarding: disabled
  IP icmp unreachables (except port): disabled
  IP icmp port-unreachable: enabled
  IP unicast reverse path forwarding: none
  IP load sharing: none
  IP interface statistics last reset: never
  IP interface software stats: (sent/received/forwarded/originated/consumed)
    Unicast packets    : 4/4/0/14/18
    Unicast bytes      : 408/336/0/1248/1512
    Multicast packets  : 0/0/0/0/0
    Multicast bytes    : 0/0/0/0/0
    Broadcast packets  : 0/0/0/0/0
    Broadcast bytes    : 0/0/0/0/0
    Labeled packets    : 0/0/0/0/0
    Labeled bytes      : 0/0/0/0/0
  WCCP Redirect outbound: disabled
  WCCP Redirect inbound: disabled
  WCCP Redirect exclude: disabled
"""


def test_nxosssh_get_interfaces_ip_post_missing_data(client):
    data = {"show_ip_interface_vrf_default": ip_interfaces}
    response = client.post("/test-getters/nxos_ssh/get_interfaces_ip", data=data)

    assert b"show ipv6 interface vrf default" in response.data
    assert b"Output from get_interfaces_ip" not in response.data
    assert b"Copy and paste the output below" not in response.data
