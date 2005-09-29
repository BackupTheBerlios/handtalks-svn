#!/usr/bin/env python
# -*- coding: latin-1 -*-

import sys

def toca_tudo (name, card=0):
    for ext in ['ogg', 'mp3', 'wav']:
        try:
            toca (name + '.' + ext, card)
        except IOError:
            pass
        except:
            return False
        else:
            return True
    return False

def toca (name, card=0):
    import pymedia.muxer as muxer
    import pymedia.audio.acodec as acodec
    import pymedia.audio.sound as sound
    import time,wave
    snds = sound.getODevices ()
    if card not in range (len (snds)):
        raise 'Cannot play sound to non existent device %d out of %d' % (card+1, len(snds))
    ext = name.split('.')[-1].lower()
    if ext == 'wav':
        f = wave.open (name, 'rb')
        snd = sound.Output (f.getframerate(), f.getnchannels(), sound.AFMT_S16_LE, card)
        s= ' '
        while len(s):
            s = f.readframes (512)
            snd.play (s)
    else:
        dm = muxer.Demuxer (ext)
        f = open (name, 'rb')
        snd = dec = None
        s = f.read (32*1024)
        t = 0
        while len (s):
            frames = dm.parse (s)
            if frames:
                for fr in frames:
                    # Assume for now only audio streams
                    if dec == None:
                        dec = acodec.Decoder (dm.streams[fr[0]])
              
                    r = dec.decode (fr[1])
                    if r and r.data:
                        if snd == None:
                            snd = sound.Output (r.sample_rate, r.channels, sound.AFMT_S16_LE, card)
                        snd.play (r.data)
              
            s = f.read (512)

    while snd.isPlaying():
        time.sleep (.05)


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print "Usage: aplayer <filename> [ sound_card_index ]"
    else:
        i= 0
        if len(sys.argv) > 2 :
            i = int (sys.argv[2])
        if not toca_tudo (sys.argv[1], i):
            print "Arquivo não encontrado!"

if __name__ == '__main__':
    main()

# vim:sw=4
