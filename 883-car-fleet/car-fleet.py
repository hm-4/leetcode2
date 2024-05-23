class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        if we sort the array then the reaching times has the following charectaristics
        target: 12, target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
        --------------------
        reaching times: a for 10, b for 11 ....
          0123456789abcd
        10: *

        08: *


        05:       *

        03:   *


        00:            *

        from top every peak is one fleet.!
        for example fleet is at 10, 05, and 00. therefore three fleets for this example
        """
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
        
        