"""Praktikum 2 - Inheritance: Hierarki Perangkat Jaringan Kampus."""


class NetworkDevice:
    def __init__(self, device_id: str, brand: str, ip_address: str):
        self.device_id = device_id
        self.brand = brand
        self.ip_address = ip_address

    def get_status(self) -> str:
        return (f"[DEVICE] ID: {self.device_id} | Brand: {self.brand} | "
                f"IP: {self.ip_address}")


class RouterNode(NetworkDevice):
    def __init__(self, device_id: str, brand: str, ip_address: str,
                 routing_table_size: int):
        super().__init__(device_id, brand, ip_address)
        self.routing_table_size = routing_table_size

    def get_status(self) -> str:
        return (f"[ROUTER] {super().get_status()} | "
                f"Routing Table: {self.routing_table_size} entri")


class SwitchNode(NetworkDevice):
    def __init__(self, device_id: str, brand: str, ip_address: str,
                 total_ports: int, vlan_count: int):
        super().__init__(device_id, brand, ip_address)
        self.total_ports = total_ports
        self.vlan_count = vlan_count

    def get_status(self) -> str:
        return (f"[SWITCH] {super().get_status()} | "
                f"Ports: {self.total_ports} | VLAN: {self.vlan_count}")


if __name__ == "__main__":
    router = RouterNode("RTR-01", "Mikrotik", "192.168.1.1", 1200)
    switch = SwitchNode("SW-01", "Cisco", "192.168.1.2", 48, 10)
    perangkat = [NetworkDevice("GEN-01", "Generic", "192.168.1.100"),
                 router, switch]
    for p in perangkat:
        print(p.get_status())

    print("\n[VERIFIKASI HIERARKI]")
    print("router instance NetworkDevice?", isinstance(router, NetworkDevice))
    print("SwitchNode subclass NetworkDevice?",
          issubclass(SwitchNode, NetworkDevice))
    print("switch instance RouterNode?", isinstance(switch, RouterNode))
    print("MRO RouterNode:", [c.__name__ for c in RouterNode.__mro__])
