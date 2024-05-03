class BroadcastEvent:
    def __init__(self, event_id, event_name, event_date,scheduled_time,channel):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.scheduled_time = scheduled_time
        self.channel = channel

    def __str__(self):
        return f"{self.event_name} - Date: {self.event_date}, Time:{self.scheduled_time},channel: {self.channel}"

class Right:
    def __init__(self, right_id, right_name, right_type, right_holder):
        self.right_id = right_id
        self.right_name = right_name
        self.right_type = right_type
        self.right_holder = right_holder

    def __str__(self):
        return f"{self.right_name} - Type: {self.right_type}, Holder: {self.right_holder}"

class BroadcastManager:
    def __init__(self):
        self.broadcasts = {}
        self.rights = {}
    def get_right(self, right_id):
        return self.rights.get(right_id)
    def is_event_id_exists(self, event_id):
        return event_id in self.broadcasts

    def add_broadcast_event(self, event):
        self.broadcasts[event.event_id] = event

    def delete_broadcast_event(self, event_id):
        self.broadcasts.pop(event_id, None)  # Remove the event if it exists, ignore otherwise

    def get_broadcast_event(self, event_id):
        return self.broadcasts.get(event_id)

    def update_broadcast_event(self, event_id, event_name, event_date, scheduled_time, channel):
        self.broadcasts[event_id].event_name = event_name
        self.broadcasts[event_id].event_date = event_date
        self.broadcasts[event_id].scheduled_time = scheduled_time
        self.broadcasts[event_id].channel = channel

    def add_right(self, right):
        self.rights[right.right_id] = right

    def delete_right(self, right_id):
        self.rights.pop(right_id, None)


    def schedule_sporting_events_broadcast(self, event_date):
        events_on_date = [event for event in self.broadcasts.values() if event.event_date == event_date]
        if events_on_date:
            print(f"Broadcast scheduled for {event_date}:")
            for event in events_on_date:
                print(f"Event ID: {event.event_id} - {event.event_name} at {event.scheduled_time}, channel: {event.channel}")
        else:
            print(f"No events scheduled for {event_date}.")
import unittest

class Broadcast:
    def __init__(self, event_id, event_name, event_date, scheduled_time, channel):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.scheduled_time = scheduled_time
        self.channel = channel

class Right:
    def __init__(self, right_id, right_type, right_holder, valid_until):
        self.right_id = right_id
        self.right_type = right_type
        self.right_holder = right_holder
        self.valid_until = valid_until

class TestBroadcastManager(unittest.TestCase):
    def setUp(self):
        self.manager = BroadcastManager()

    def test_add_broadcast_event(self):
        event = Broadcast(1, "Football Match", "2024-05-01", "15:00", "ESPN")
        self.manager.add_broadcast_event(event)
        self.assertTrue(self.manager.is_event_id_exists(1))

    def test_delete_broadcast_event(self):
        event = Broadcast(2, "Basketball Game", "2024-05-02", "17:00", "ABC")
        self.manager.add_broadcast_event(event)
        self.manager.delete_broadcast_event(2)
        self.assertFalse(self.manager.is_event_id_exists(2))

    def test_get_broadcast_event(self):
        event = Broadcast(3, "Tennis Tournament", "2024-05-03", "13:00", "CBS")
        self.manager.add_broadcast_event(event)
        retrieved_event = self.manager.get_broadcast_event(3)
        self.assertEqual(retrieved_event.event_name, "Tennis Tournament")

    def test_update_broadcast_event(self):
        event = Broadcast(4, "Soccer Game", "2024-05-04", "19:00", "FOX")
        self.manager.add_broadcast_event(event)
        self.manager.update_broadcast_event(4, "Updated Soccer Game", "2024-05-04", "19:30", "FOX")
        updated_event = self.manager.get_broadcast_event(4)
        self.assertEqual(updated_event.event_name, "Updated Soccer Game")

    def test_add_right(self):
        right = Right(1, "Streaming", "Company A", "2025-01-01")
        self.manager.add_right(right)
        self.assertIsNotNone(self.manager.get_right(1))

    def test_delete_right(self):
        right = Right(2, "Broadcasting", "Company B", "2025-01-01")
        self.manager.add_right(right)
        self.manager.delete_right(2)
        self.assertIsNone(self.manager.get_right(2))

    def test_schedule_sporting_events_broadcast(self):
        event1 = Broadcast(5, "Golf Tournament", "2024-05-05", "14:00", "Golf Channel")
        event2 = Broadcast(6, "Sailing Race", "2024-05-05", "15:00", "ESPN")
        self.manager.add_broadcast_event(event1)
        self.manager.add_broadcast_event(event2)
        # Redirect stdout to catch print statements
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            self.manager.schedule_sporting_events_broadcast("2024-05-05")
            output = out.getvalue().strip()
            self.assertIn("Broadcast scheduled for 2024-05-05:", output)
            self.assertIn("Event ID: 5 - Golf Tournament at 14:00, channel: Golf Channel", output)
            self.assertIn("Event ID: 6 - Sailing Race at 15:00, channel: ESPN", output)
        finally:
            sys.stdout = saved_stdout

if __name__ == '__main__':
    unittest.main(verbosity=8,exit=False)