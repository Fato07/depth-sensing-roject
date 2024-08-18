class AlertSystem:
    def __init__(self, critical_distance):
        self.critical_distance = critical_distance

    def check_for_obstacles(self, objects):
        alerts = []
        for x, y, distance in objects:
            if distance < self.critical_distance:
                alerts.append(f"Warning: Object detected at ({x}, {y}) at distance {distance:.2f}m")
        return alerts

    def print_alerts(self, alerts):
        if alerts:
            print("ALERTS:")
            for alert in alerts:
                print(alert)
        else:
            print("No obstacles detected within critical distance.")