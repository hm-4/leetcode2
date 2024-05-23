class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleet = 0
        # caluclate times
        individual_times = []
        position_speed = sorted(zip(position, speed), reverse=True)
        last_peak = -1
        # print(position_speed)
        for position, speed in position_speed:
            reaching_time = (target-position) / speed
            # print(reaching_time)
            if reaching_time > last_peak:
                fleet += 1
                last_peak = reaching_time
        return fleet
        
        