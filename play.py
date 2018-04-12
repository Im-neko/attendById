import pyaudio
import wave

def sugoi():
    input_filename = 'sounds/nc154074.wav'
    buffer_size = 4096
    wav_file = wave.open ( input_filename , 'rb' )
    p = pyaudio.PyAudio ()
    stream = p.open (
                     format = p.get_format_from_width ( wav_file . getsampwidth ()) ,
                     channels = wav_file.getnchannels () ,
                     rate = wav_file.getframerate () ,
                     output = True
                     )
    remain = wav_file.getnframes ()
    while remain > 0:
        buf = wav_file.readframes ( min ( buffer_size , remain ))
        stream.write ( buf )
        remain -= buffer_size

    stream.close ()
    p.terminate ()
    wav_file.close ()

def pinpon():
    input_filename = 'sounds/pinpon.wav'
    buffer_size = 4096
    wav_file = wave.open ( input_filename , 'rb' )
    p = pyaudio.PyAudio ()
    stream = p.open (
                     format = p.get_format_from_width ( wav_file . getsampwidth ()) ,
                     channels = wav_file.getnchannels () ,
                     rate = wav_file.getframerate () ,
                     output = True
                     )
    remain = wav_file.getnframes ()
    while remain > 0:
        buf = wav_file.readframes ( min ( buffer_size , remain ))
        stream.write ( buf )
        remain -= buffer_size

    stream.close ()
    p.terminate ()
    wav_file.close ()

def bubu():
    input_filename = 'sounds/bububu.wav'
    buffer_size = 4096
    wav_file = wave.open ( input_filename , 'rb' )
    p = pyaudio.PyAudio ()
    stream = p.open (
                     format = p.get_format_from_width ( wav_file . getsampwidth ()) ,
                     channels = wav_file.getnchannels () ,
                     rate = wav_file.getframerate () ,
                     output = True
                     )
    remain = wav_file.getnframes ()
    while remain > 0:
        buf = wav_file.readframes ( min ( buffer_size , remain ))
        stream.write ( buf )
        remain -= buffer_size

    stream.close ()
    p.terminate ()
    wav_file.close ()
    
def deden():
    input_filename = 'sounds/deden.wav'
    buffer_size = 4096
    wav_file = wave.open ( input_filename , 'rb' )
    p = pyaudio.PyAudio ()
    stream = p.open (
                     format = p.get_format_from_width ( wav_file . getsampwidth ()) ,
                     channels = wav_file.getnchannels () ,
                     rate = wav_file.getframerate () ,
                     output = True
                     )
    remain = wav_file.getnframes ()
    while remain > 0:
        buf = wav_file.readframes ( min ( buffer_size , remain ))
        stream.write ( buf )
        remain -= buffer_size

    stream.close ()
    p.terminate ()
    wav_file.close ()
