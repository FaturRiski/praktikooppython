"""Praktikum 1 - Encapsulation: Pengolahan Sensor IoT (SensorDataNode)."""


class SensorDataNode:
    TEMP_MIN = -10.0
    TEMP_MAX = 60.0

    def __init__(self, node_id: str, location: str,
                 temperature: float, humidity: float):
        self.node_id = node_id            # Public
        self.location = location          # Public
        self.__temperature = 0.0          # Private
        self.__humidity = 0.0             # Private
        self.temperature = temperature    # lewat setter (tervalidasi)
        self.__humidity = max(0.0, min(100.0, humidity))

    @property
    def temperature(self) -> float:
        """Getter suhu (private)."""
        return self.__temperature

    @temperature.setter
    def temperature(self, value: float):
        """Setter suhu: hanya menerima -10.0 s.d. 60.0 derajat C."""
        if self.TEMP_MIN <= value <= self.TEMP_MAX:
            self.__temperature = float(value)
            print(f"[SUCCESS] Suhu {self.node_id} diperbarui: {value} C")
        else:
            print(f"[ERROR] Suhu {value} C ditolak! Rentang valid "
                  f"{self.TEMP_MIN} s.d. {self.TEMP_MAX} C.")

    @property
    def humidity(self) -> float:
        """Getter kelembapan (read-only)."""
        return self.__humidity

    def get_status_summary(self) -> str:
        return (f"[NODE {self.node_id}] Lokasi: {self.location} | "
                f"Suhu: {self.__temperature:.1f} C | "
                f"Kelembapan: {self.__humidity:.1f}%")


if __name__ == "__main__":
    node = SensorDataNode("IOT-01", "Lab Komputer UNTARA", 27.5, 65.0)
    print(node.get_status_summary())

    print("\n--- Uji suhu valid ---")
    node.temperature = 35.0
    node.temperature = -10.0
    node.temperature = 60.0

    print("\n--- Uji suhu di luar rentang (harus ditolak) ---")
    node.temperature = 75.0
    node.temperature = -15.5
    print("Suhu tetap:", node.temperature)
    assert node.temperature == 60.0

    print("\n--- Uji akses langsung atribut private ---")
    try:
        print(node.__temperature)
    except AttributeError as e:
        print(f"[AKSES DITOLAK] {e}")
    print(node.get_status_summary())
