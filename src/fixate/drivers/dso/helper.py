import inspect
from abc import ABCMeta, abstractmethod
from functools import update_wrapper
from fixate.core.exceptions import InstrumentFeatureUnavailable

import typing

number = typing.Union[float, int]


class CallableNoArgs:
    def __call__(self):
        return self._call()

    def _call(self):
        raise InstrumentFeatureUnavailable()


class CallableBool:
    def __call__(self, value: bool):
        return self._call(value)

    def _call(self, value: bool):
        raise InstrumentFeatureUnavailable()


class SourcesCh:
    def ch1(self):
        raise InstrumentFeatureUnavailable()

    def ch2(self):
        raise InstrumentFeatureUnavailable()

    def ch3(self):
        raise InstrumentFeatureUnavailable()

    def ch4(self):
        raise InstrumentFeatureUnavailable()


class SourcesSpecial:
    def function(self):
        raise InstrumentFeatureUnavailable()

    def math(self):
        raise InstrumentFeatureUnavailable()


class SourcesWMem:
    def wmemory1(self):
        raise InstrumentFeatureUnavailable()

    def wmemory2(self):
        raise InstrumentFeatureUnavailable()


class SourcesExt:
    def external(self):
        raise InstrumentFeatureUnavailable()


class SourcesDig:
    def d0(self):
        raise InstrumentFeatureUnavailable()

    def d1(self):
        raise InstrumentFeatureUnavailable()

    def d2(self):
        raise InstrumentFeatureUnavailable()

    def d3(self):
        raise InstrumentFeatureUnavailable()

    def d4(self):
        raise InstrumentFeatureUnavailable()

    def d5(self):
        raise InstrumentFeatureUnavailable()

    def d6(self):
        raise InstrumentFeatureUnavailable()

    def d7(self):
        raise InstrumentFeatureUnavailable()

    def d8(self):
        raise InstrumentFeatureUnavailable()

    def d9(self):
        raise InstrumentFeatureUnavailable()

    def d10(self):
        raise InstrumentFeatureUnavailable()

    def d11(self):
        raise InstrumentFeatureUnavailable()

    def d12(self):
        raise InstrumentFeatureUnavailable()

    def d13(self):
        raise InstrumentFeatureUnavailable()

    def d14(self):
        raise InstrumentFeatureUnavailable()

    def d15(self):
        raise InstrumentFeatureUnavailable()


class MeasureAllSources(
    SourcesCh, SourcesSpecial, SourcesWMem, SourcesDig, CallableNoArgs
):
    pass


class TrigSources(SourcesCh, SourcesExt, SourcesDig):
    pass


class MultiMeasureSources(MeasureAllSources):
    def __init__(self):
        self.ch1 = MeasureAllSources()
        self.ch1 = MeasureAllSources()
        self.ch2 = MeasureAllSources()
        self.ch3 = MeasureAllSources()
        self.ch4 = MeasureAllSources()
        self.function = MeasureAllSources()
        self.math = MeasureAllSources()
        self.wmemory1 = MeasureAllSources()
        self.wmemory2 = MeasureAllSources()
        self.external = MeasureAllSources()
        self.d0 = MeasureAllSources()
        self.d1 = MeasureAllSources()
        self.d2 = MeasureAllSources()
        self.d3 = MeasureAllSources()
        self.d4 = MeasureAllSources()
        self.d5 = MeasureAllSources()
        self.d6 = MeasureAllSources()
        self.d7 = MeasureAllSources()
        self.d8 = MeasureAllSources()
        self.d9 = MeasureAllSources()
        self.d10 = MeasureAllSources()
        self.d11 = MeasureAllSources()
        self.d12 = MeasureAllSources()
        self.d13 = MeasureAllSources()
        self.d14 = MeasureAllSources()
        self.d15 = MeasureAllSources()


class Coupling:
    def ac(self):
        raise InstrumentFeatureUnavailable()

    def dc(self):
        raise InstrumentFeatureUnavailable()

    def lf_reject(self):
        raise InstrumentFeatureUnavailable()

    def tv(self):
        raise InstrumentFeatureUnavailable()


class Probe:
    def attenuation(self, value: number):
        raise InstrumentFeatureUnavailable()


class VerticalUnits:
    def volts(self):
        raise InstrumentFeatureUnavailable()

    def amps(self):
        raise InstrumentFeatureUnavailable()


class ChannelBase(CallableBool):
    def __init__(self, channel_name: str):
        self._ch_name = channel_name
        # self.waveform = Waveform()
        # self.modulate = Modulate()
        # self.burst = Burst()
        # self.load = Load()
        self.coupling = Coupling()
        self.probe = Probe()
        self.units = VerticalUnits()

    def bandwidth(self, value: number):
        raise InstrumentFeatureUnavailable()

    def bandwidth_limit(self, value: bool):
        raise InstrumentFeatureUnavailable()

    def impedance(self, value: number):
        raise InstrumentFeatureUnavailable()

    def invert(self, value: bool):
        raise InstrumentFeatureUnavailable()

    def offset(self, value: number):
        raise InstrumentFeatureUnavailable()

    def scale(self, value: number):
        raise InstrumentFeatureUnavailable()


class Trigger:
    def __init__(self):
        self.mode = TrigMode()
        self.delay = None
        self.eburst = None
        self.coupling = Coupling()
        self.sweep = TrigSweep()

    def force(self):
        raise InstrumentFeatureUnavailable()

    def hf_reject(self, value: bool):
        raise InstrumentFeatureUnavailable()

    def hold_off(self, value: number):
        raise InstrumentFeatureUnavailable()

    def n_reject(self, value: bool):
        raise InstrumentFeatureUnavailable()


class TrigSweep:
    def auto(self):
        raise InstrumentFeatureUnavailable()

    def normal(self):
        raise InstrumentFeatureUnavailable()


class TrigLevel:
    def high(self, value: number):
        raise InstrumentFeatureUnavailable()

    def low(self, value: number):
        raise InstrumentFeatureUnavailable()


class TrigMode:
    def __init__(self):
        self.edge = TrigEdge()


class TrigEdge(CallableNoArgs):
    def __init__(self):
        self.source = TrigSources()
        self.slope = Slopes()

    def level(self, value: number):
        raise InstrumentFeatureUnavailable()


class TrigReject:
    def off(self):
        raise InstrumentFeatureUnavailable()

    def lf(self):
        raise InstrumentFeatureUnavailable()

    def hf(self):
        raise InstrumentFeatureUnavailable()


class Slopes:
    def rising(self):
        raise InstrumentFeatureUnavailable()

    def falling(self):
        raise InstrumentFeatureUnavailable()

    def alternating(self):
        raise InstrumentFeatureUnavailable()

    def either(self):
        raise InstrumentFeatureUnavailable()


class Acquire:
    def __init__(self):
        self.mode = AcquireMode()

    def normal(self):
        raise InstrumentFeatureUnavailable()

    def peak_detect(self):
        raise InstrumentFeatureUnavailable()

    def averaging(self, value: number):
        raise InstrumentFeatureUnavailable()

    def high_resolution(self):
        raise InstrumentFeatureUnavailable()


class AcquireMode:
    def rtim(self):
        raise InstrumentFeatureUnavailable()

    def segm(self):
        raise InstrumentFeatureUnavailable()


class Timebase:
    def __init__(self):
        self.mode = TimebaseMode()

    def position(self, value: number):
        raise InstrumentFeatureUnavailable()

    def scale(self, value: number):
        raise InstrumentFeatureUnavailable()


class TimebaseMode:
    def main(self):
        raise InstrumentFeatureUnavailable()

    def window(self):
        raise InstrumentFeatureUnavailable()

    def xy(self):
        raise InstrumentFeatureUnavailable()

    def roll(self):
        raise InstrumentFeatureUnavailable()


class Events:
    def trigger(self):
        """
        Indicates if a trigger event has occurred.
        Calls to this will clear the existing trigger events
        :return:
        """
        raise InstrumentFeatureUnavailable()


class MeasureInterval:
    def __init__(self):
        self.cycle = MeasureAllSources()
        self.display = MeasureAllSources()


class MeasureIntervalMultipleSources:
    def __init__(self):
        self.cycle = MultiMeasureSources()
        self.display = MultiMeasureSources()


class MeasureRMS:
    def __init__(self):
        self.dc = MeasureInterval()
        self.ac = MeasureInterval()


class Threshold:
    def percent(self, upper: number, middle: number, lower: number):
        """
        :param upper: Upper Threshold
        :param middle: Middle Threshold
        :param lower: Lower Threshold
        :return:
        """
        raise InstrumentFeatureUnavailable()

    def absolute(self, upper: number, middle: number, lower: number):
        """
        :param upper: Upper Threshold
        :param middle: Middle Threshold
        :param lower: Lower Threshold
        :return:
        """
        raise InstrumentFeatureUnavailable()


class Define:
    def __init__(self):
        super().__init__()
        self.threshold = Threshold()


class Delay(CallableNoArgs):
    def __init__(self):
        super().__init__()
        self.edges = MultiSlopes()


class Measure:
    def __init__(self):
        self.counter = MeasureAllSources()
        self.define = Define()
        self.delay = Delay()
        self.duty = MeasureAllSources()
        self.fall_time = MeasureAllSources()
        self.rise_time = MeasureAllSources()
        self.frequency = MeasureAllSources()
        self.cnt_edge_rising = MeasureAllSources()
        self.cnt_edge_falling = MeasureAllSources()
        self.cnt_pulse_positive = MeasureAllSources()
        self.cnt_pulse_negative = MeasureAllSources()
        self.period = MeasureAllSources()
        self.phase = MultiMeasureSources()
        self.pulse_width = MeasureAllSources()
        self.vamplitude = MeasureAllSources()
        self.vaverage = MeasureInterval()
        self.vbase = MeasureAllSources()
        self.vtop = MeasureAllSources()
        self.vmax = MeasureAllSources()
        self.vmin = MeasureAllSources()
        self.vpp = MeasureAllSources()
        self.vratio = MeasureIntervalMultipleSources()
        self.vrms = MeasureRMS()
        self.xmax = MeasureAllSources()
        self.xmin = MeasureAllSources()


class MultiSlopes(CallableNoArgs):
    def __init__(self):
        super().__init__()
        self.rising = Slopes()
        self.falling = Slopes()
        self.alternating = Slopes()
        self.either = Slopes()


class DSO(metaclass=ABCMeta):
    REGEX_ID = "DSO"

    def __init__(self, instrument):
        self.instrument = instrument
        self.samples = 1
        self.api = []
        self.ch1 = ChannelBase("1")
        self.ch2 = ChannelBase("2")
        self.ch3 = ChannelBase("3")
        self.ch4 = ChannelBase("4")
        self.chmath = ChannelBase("math")
        self.chfunc = ChannelBase("func")
        self.coupling = Coupling()
        self.probe = Probe()
        self.source1 = MultiMeasureSources()
        self.source2 = MultiMeasureSources()
        self.trigger = Trigger()
        self.time_base = Timebase()
        self.acquire = Acquire()
        self.measure = Measure()
        self.events = Events()

    @abstractmethod
    def acquire(self, acquire_type, averaging_samples):
        pass

    @abstractmethod
    def waveform_values(self, source, filename):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def auto_scale(self):
        pass

    @abstractmethod
    def save_setup(self, file_name):
        pass

    @abstractmethod
    def load_setup(self, file_name):
        pass

    @abstractmethod
    def get_identity(self):
        pass

    def run(self):
        raise InstrumentFeatureUnavailable()

    def single(self):
        raise InstrumentFeatureUnavailable()

    def stop(self):
        raise InstrumentFeatureUnavailable()

    def scale(self, value: number):
        raise InstrumentFeatureUnavailable()

    def offset(self, value: number):
        raise InstrumentFeatureUnavailable()

    def init_api(self):
        for func_str, handler, base_str in self.api:
            *parents, func = func_str.split(".")
            parent_obj = self
            for parent in parents:
                parent_obj = getattr(parent_obj, parent)
            func_obc = getattr(parent_obj, func)
            setattr(parent_obj, func, self.prepare_string(func_obc, handler, base_str))

    def prepare_string(self, func, handler, base_str, *args, **kwargs):
        def temp_func(*nargs, **nkwargs):
            """
            Only formats using **nkwargs
            New Temp
            :param nargs:
            :param nkwargs:
            :return:
            """
            sig = inspect.signature(func)
            keys = [itm[0] for itm in sig.parameters.items()]
            for index, param in enumerate(nargs):
                nkwargs[keys[index]] = param
            # new_str = base_str.format(**nkwargs)
            # handler(self, new_str)
            return handler(base_str, **nkwargs)

        return update_wrapper(temp_func, func)
