import EPD_Display
import time
import machine
import utime


# Display resolution
EPD_WIDTH       = 128
EPD_HEIGHT      = 296

class EPD_Clock:
    def __init__(self, epd):
        self.epd = epd
        self.screen_width = 128
        self.screen_height = 296
        self.padding = 10
        self.segment_width = self.screen_width - 2 * self.padding
        self.segment_height = self.screen_height // 4 - 2 * self.padding
        self.thickness = 10
        self.segments = {
            0: {'a': True, 'b': True, 'c': True, 'd': True, 'e': True, 'f': True, 'g': False},
            1: {'a': False, 'b': True, 'c': True, 'd': False, 'e': False, 'f': False, 'g': False},
            2: {'a': True, 'b': True, 'c': False, 'd': True, 'e': True, 'f': False, 'g': True},
            3: {'a': True, 'b': True, 'c': True, 'd': True, 'e': False, 'f': False, 'g': True},
            4: {'a': False, 'b': True, 'c': True, 'd': False, 'e': False, 'f': True, 'g': True},
            5: {'a': True, 'b': False, 'c': True, 'd': True, 'e': False, 'f': True, 'g': True},
            6: {'a': True, 'b': False, 'c': True, 'd': True, 'e': True, 'f': True, 'g': True},
            7: {'a': True, 'b': True, 'c': True, 'd': False, 'e': False, 'f': False, 'g': False},
            8: {'a': True, 'b': True, 'c': True, 'd': True, 'e': True, 'f': True, 'g': True},
            9: {'a': True, 'b': True, 'c': True, 'd': True, 'e': False, 'f': True, 'g': True},
            "Test": {'a': True, 'b': True, 'c': False, 'd': False, 'e': False, 'f': True, 'g': True}
        }


        # Initialize RTC
        self.rtc = machine.RTC()

    
    def update_time(self):
        
        rtc_datetime = self.rtc.datetime()

        # Convert RTC datetime to a human-readable format
        hour = rtc_datetime[4]
        minute = rtc_datetime[5]
        second = rtc_datetime[6]
        
        current_time = list("{:02}{:02}".format(hour, minute))
        print(current_time)
        self.draw_segment_1(current_time[0])
        self.draw_segment_2(current_time[1])
        self.draw_segment_3(current_time[2])
        self.draw_segment_4(current_time[3])
        self.epd.display()
        
        time.sleep(60)
        
        self.update_time()
        
        

    def draw_segment(self, x_offset, y_offset, segments):
        x_inner_offset = x_offset + self.padding
        y_inner_offset = y_offset + self.padding

        if segments['a']:
            self.epd.imageblack.fill_rect(x_inner_offset + self.segment_width - self.thickness, y_inner_offset, self.thickness, self.segment_height, 0x00) # DONE
        if segments['b']:
            self.epd.imageblack.fill_rect(x_inner_offset + (self.segment_width // 2) - (self.thickness // 2), y_inner_offset+self.segment_height-self.thickness, (self.segment_width // 2), self.thickness, 0x00) # DONE
        if segments['c']:
            self.epd.imageblack.fill_rect(x_inner_offset, y_inner_offset+self.segment_height-self.thickness, (self.segment_width // 2), self.thickness, 0x00) # DONE
        if segments['d']:
            self.epd.imageblack.fill_rect(x_inner_offset, y_inner_offset, self.thickness, self.segment_height, 0x00) # DONE
        if segments['e']:
            self.epd.imageblack.fill_rect(x_inner_offset, y_inner_offset, (self.segment_width // 2), self.thickness, 0x00) # DONE
        if segments['f']:
            self.epd.imageblack.fill_rect(x_inner_offset + (self.segment_width // 2) - (self.thickness // 2), y_inner_offset, (self.segment_width // 2), self.thickness, 0x00) # DONE
        if segments['g']:
            self.epd.imageblack.fill_rect(x_inner_offset + (self.segment_width // 2) - (self.thickness // 2), y_inner_offset, self.thickness, self.segment_height, 0x00) # DONE

    def draw_segment_1(self, digit):
        x_offset = 0
        y_offset = 0
        self.draw_segment(x_offset, y_offset, self.segments[int(digit)])

    def draw_segment_2(self, digit):
        x_offset = 0
        y_offset = self.screen_height // 4
        self.draw_segment(x_offset, y_offset, self.segments[int(digit)])

    def draw_segment_3(self, digit):
        x_offset = 0
        y_offset = 2 * (self.screen_height // 4)
        self.draw_segment(x_offset, y_offset, self.segments[int(digit)])

    def draw_segment_4(self, digit):
        x_offset = 0
        y_offset = 3 * (self.screen_height // 4)
        self.draw_segment(x_offset, y_offset, self.segments[int(digit)])






if __name__=='__main__':
    epd = EPD_Display.EPD_2in9_B()
    clock = EPD_Clock(epd)
    clock.update_time()

    
    
    

