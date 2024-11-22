


class Television():
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes attributes of an instance of a Television
        :return: None
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Takes an instance of Television as input and toggles its on/off status
        :return: None
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Takes an instance of Television as input and, if it's on, toggles
        whether it's muted
        :return: None
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Takes an instance of Television as input and, if it's on, increases the
        channel value by 1. If its channel is at the channel maximum it will
        loop around to the minimum channel
        :return: None
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Takes an instance of Television as input and, if it's on, decreases the
        channel value by 1. If its channel is at the channel minimum it will
        loop around to the maximum channel
        :return: None
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Takes an instance of Television as input and, if it's on, increases the
        volume by 1. If its volume is at the volume maximum it will remain at
        the volume maximum
        :return: None
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Takes an instance of Television as input and, if it's on, decreases the
        volume by 1. If its volume is at the volume minimum it will remain at
        the volume minimum
        :return: None
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Takes an instance of Television as input and returns a string containing
        information on whether the Television is on, what channel it's on, and
        what volume it's at. If the Television is muted the string will say the
        Television's volume is 0 regardless of its value.
        NOTE: though the string will show volume as 0 if the Television is muted,
        this will not change the volume value of the Television.
        :return: str
        """
        if self.__muted:
            strVol: int = Television.MIN_VOLUME
        else:
            strVol: int = self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {strVol}'

