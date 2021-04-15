from pathlib import Path
from datetime import datetime
from unittest import mock

import numpy as np

import astropy.units as u
from astropy.time import Time
from sunpy.net import attrs as a

from radiospectra.spectrogram2 import Spectrogram
from radiospectra.spectrogram2.sources import RSTNSpectrogram


@mock.patch('radiospectra.spectrogram2.spectrogram.SpectrogramFactory._read_srs')
def test_rstn(read_srs):
    start_time = Time('2020-01-01T06:17:38.000')
    end_time = Time('2020-01-01T15:27:43.000')
    meta = {
        'instrument': 'RSTN',
        'observatory': 'San Vito',
        'start_time': start_time,
        'end_time': end_time,
        'detector': 'RSTN',
        'wavelength': a.Wavelength(25000.0 * u.kHz, 180000.0 * u.kHz),
        'freqs': [25., 25.125, 25.25, 25.375, 25.5, 25.625, 25.75, 25.875, 26., 26.125, 26.25,
                  26.375, 26.5, 26.625, 26.75, 26.875, 27., 27.125, 27.25, 27.375, 27.5, 27.625,
                  27.75, 27.875, 28., 28.125, 28.25, 28.375, 28.5, 28.625, 28.75, 28.875, 29.,
                  29.125, 29.25, 29.375, 29.5, 29.625, 29.75, 29.875, 30., 30.125, 30.25, 30.375,
                  30.5, 30.625, 30.75, 30.875, 31., 31.125, 31.25, 31.375, 31.5, 31.625, 31.75,
                  31.875, 32., 32.125, 32.25, 32.375, 32.5, 32.625, 32.75, 32.875, 33., 33.125,
                  33.25, 33.375, 33.5, 33.625, 33.75, 33.875, 34., 34.125, 34.25, 34.375, 34.5,
                  34.625, 34.75, 34.875, 35., 35.125, 35.25, 35.375, 35.5, 35.625, 35.75, 35.875,
                  36., 36.125, 36.25, 36.375, 36.5, 36.625, 36.75, 36.875, 37., 37.125, 37.25,
                  37.375, 37.5, 37.625, 37.75, 37.875, 38., 38.125, 38.25, 38.375, 38.5, 38.625,
                  38.75, 38.875, 39., 39.125, 39.25, 39.375, 39.5, 39.625, 39.75, 39.875, 40.,
                  40.125, 40.25, 40.375, 40.5, 40.625, 40.75, 40.875, 41., 41.125, 41.25, 41.375,
                  41.5, 41.625, 41.75, 41.875, 42., 42.125, 42.25, 42.375, 42.5, 42.625, 42.75,
                  42.875, 43., 43.125, 43.25, 43.375, 43.5, 43.625, 43.75, 43.875, 44., 44.125,
                  44.25, 44.375, 44.5, 44.625, 44.75, 44.875, 45., 45.125, 45.25, 45.375, 45.5,
                  45.625, 45.75, 45.875, 46., 46.125, 46.25, 46.375, 46.5, 46.625, 46.75, 46.875,
                  47., 47.125, 47.25, 47.375, 47.5, 47.625, 47.75, 47.875, 48., 48.125, 48.25,
                  48.375, 48.5, 48.625, 48.75, 48.875, 49., 49.125, 49.25, 49.375, 49.5, 49.625,
                  49.75, 49.875, 50., 50.125, 50.25, 50.375, 50.5, 50.625, 50.75, 50.875, 51.,
                  51.125, 51.25, 51.375, 51.5, 51.625, 51.75, 51.875, 52., 52.125, 52.25, 52.375,
                  52.5, 52.625, 52.75, 52.875, 53., 53.125, 53.25, 53.375, 53.5, 53.625, 53.75,
                  53.875, 54., 54.125, 54.25, 54.375, 54.5, 54.625, 54.75, 54.875, 55., 55.125,
                  55.25, 55.375, 55.5, 55.625, 55.75, 55.875, 56., 56.125, 56.25, 56.375, 56.5,
                  56.625, 56.75, 56.875, 57., 57.125, 57.25, 57.375, 57.5, 57.625, 57.75, 57.875,
                  58., 58.125, 58.25, 58.375, 58.5, 58.625, 58.75, 58.875, 59., 59.125, 59.25,
                  59.375, 59.5, 59.625, 59.75, 59.875, 60., 60.125, 60.25, 60.375, 60.5, 60.625,
                  60.75, 60.875, 61., 61.125, 61.25, 61.375, 61.5, 61.625, 61.75, 61.875, 62.,
                  62.125, 62.25, 62.375, 62.5, 62.625, 62.75, 62.875, 63., 63.125, 63.25, 63.375,
                  63.5, 63.625, 63.75, 63.875, 64., 64.125, 64.25, 64.375, 64.5, 64.625, 64.75,
                  64.875, 65., 65.125, 65.25, 65.375, 65.5, 65.625, 65.75, 65.875, 66., 66.125,
                  66.25, 66.375, 66.5, 66.625, 66.75, 66.875, 67., 67.125, 67.25, 67.375, 67.5,
                  67.625, 67.75, 67.875, 68., 68.125, 68.25, 68.375, 68.5, 68.625, 68.75, 68.875,
                  69., 69.125, 69.25, 69.375, 69.5, 69.625, 69.75, 69.875, 70., 70.125, 70.25,
                  70.375, 70.5, 70.625, 70.75, 70.875, 71., 71.125, 71.25, 71.375, 71.5, 71.625,
                  71.75, 71.875, 72., 72.125, 72.25, 72.375, 72.5, 72.625, 72.75, 72.875, 73.,
                  73.125, 73.25, 73.375, 73.5, 73.625, 73.75, 73.875, 74., 74.125, 74.25, 74.375,
                  74.5, 74.625, 74.75, 74.875, 75., 75., 75.2625, 75.525, 75.7875, 76.05, 76.3125,
                  76.575, 76.8375, 77.1, 77.3625, 77.625, 77.8875, 78.15, 78.4125, 78.675, 78.9375,
                  79.2, 79.4625, 79.725, 79.9875, 80.25, 80.5125, 80.775, 81.0375, 81.3, 81.5625,
                  81.825, 82.0875, 82.35, 82.6125, 82.875, 83.1375, 83.4, 83.6625, 83.925, 84.1875,
                  84.45, 84.7125, 84.975, 85.2375, 85.5, 85.7625, 86.025, 86.2875, 86.55, 86.8125,
                  87.075, 87.3375, 87.6, 87.8625, 88.125, 88.3875, 88.65, 88.9125, 89.175, 89.4375,
                  89.7, 89.9625, 90.225, 90.4875, 90.75, 91.0125, 91.275, 91.5375, 91.8, 92.0625,
                  92.325, 92.5875, 92.85, 93.1125, 93.375, 93.6375, 93.9, 94.1625, 94.425, 94.6875,
                  94.95, 95.2125, 95.475, 95.7375, 96., 96.2625, 96.525, 96.7875, 97.05, 97.3125,
                  97.575, 97.8375, 98.1, 98.3625, 98.625, 98.8875, 99.15, 99.4125, 99.675, 99.9375,
                  100.2, 100.4625, 100.725, 100.9875, 101.25, 101.5125, 101.775, 102.0375, 102.3,
                  102.5625, 102.825, 103.0875, 103.35, 103.6125, 103.875, 104.1375, 104.4, 104.6625,
                  104.925, 105.1875, 105.45, 105.7125, 105.975, 106.2375, 106.5, 106.7625, 107.025,
                  107.2875, 107.55, 107.8125, 108.075, 108.3375, 108.6, 108.8625, 109.125, 109.3875,
                  109.65, 109.9125, 110.175, 110.4375, 110.7, 110.9625, 111.225, 111.4875, 111.75,
                  112.0125, 112.275, 112.5375, 112.8, 113.0625, 113.325, 113.5875, 113.85, 114.1125,
                  114.375, 114.6375, 114.9, 115.1625, 115.425, 115.6875, 115.95, 116.2125, 116.475,
                  116.7375, 117., 117.2625, 117.525, 117.7875, 118.05, 118.3125, 118.575, 118.8375,
                  119.1, 119.3625, 119.625, 119.8875, 120.15, 120.4125, 120.675, 120.9375, 121.2,
                  121.4625, 121.725, 121.9875, 122.25, 122.5125, 122.775, 123.0375, 123.3, 123.5625,
                  123.825, 124.0875, 124.35, 124.6125, 124.875, 125.1375, 125.4, 125.6625, 125.925,
                  126.1875, 126.45, 126.7125, 126.975, 127.2375, 127.5, 127.7625, 128.025, 128.2875,
                  128.55, 128.8125, 129.075, 129.3375, 129.6, 129.8625, 130.125, 130.3875, 130.65,
                  130.9125, 131.175, 131.4375, 131.7, 131.9625, 132.225, 132.4875, 132.75, 133.0125,
                  133.275, 133.5375, 133.8, 134.0625, 134.325, 134.5875, 134.85, 135.1125, 135.375,
                  135.6375, 135.9, 136.1625, 136.425, 136.6875, 136.95, 137.2125, 137.475, 137.7375,
                  138., 138.2625, 138.525, 138.7875, 139.05, 139.3125, 139.575, 139.8375, 140.1,
                  140.3625, 140.625, 140.8875, 141.15, 141.4125, 141.675, 141.9375, 142.2, 142.4625,
                  142.725, 142.9875, 143.25, 143.5125, 143.775, 144.0375, 144.3, 144.5625, 144.825,
                  145.0875, 145.35, 145.6125, 145.875, 146.1375, 146.4, 146.6625, 146.925, 147.1875,
                  147.45, 147.7125, 147.975, 148.2375, 148.5, 148.7625, 149.025, 149.2875, 149.55,
                  149.8125, 150.075, 150.3375, 150.6, 150.8625, 151.125, 151.3875, 151.65, 151.9125,
                  152.175, 152.4375, 152.7, 152.9625, 153.225, 153.4875, 153.75, 154.0125, 154.275,
                  154.5375, 154.8, 155.0625, 155.325, 155.5875, 155.85, 156.1125, 156.375, 156.6375,
                  156.9, 157.1625, 157.425, 157.6875, 157.95, 158.2125, 158.475, 158.7375, 159.,
                  159.2625, 159.525, 159.7875, 160.05, 160.3125, 160.575, 160.8375, 161.1, 161.3625,
                  161.625, 161.8875, 162.15, 162.4125, 162.675, 162.9375, 163.2, 163.4625, 163.725,
                  163.9875, 164.25, 164.5125, 164.775, 165.0375, 165.3, 165.5625, 165.825, 166.0875,
                  166.35, 166.6125, 166.875, 167.1375, 167.4, 167.6625, 167.925, 168.1875, 168.45,
                  168.7125, 168.975, 169.2375, 169.5, 169.7625, 170.025, 170.2875, 170.55, 170.8125,
                  171.075, 171.3375, 171.6, 171.8625, 172.125, 172.3875, 172.65, 172.9125, 173.175,
                  173.4375, 173.7, 173.9625, 174.225, 174.4875, 174.75, 175.0125, 175.275, 175.5375,
                  175.8, 176.0625, 176.325, 176.5875, 176.85, 177.1125, 177.375, 177.6375, 177.9,
                  178.1625, 178.425, 178.6875, 178.95, 179.2125, 179.475, 179.7375, 180.]*u.MHz,
        'times': start_time + np.linspace(0, (end_time-start_time).to_value('s'), 11003)*u.s
    }
    array = np.zeros((802, 11003))
    read_srs.return_value = (meta, array)
    file = Path('fakes.srs')
    spec = Spectrogram(file)
    assert isinstance(spec, RSTNSpectrogram)
    assert spec.observatory == 'SAN VITO'
    assert spec.instrument == 'RSTN'
    assert spec.detector == 'RSTN'
    assert spec.start_time.datetime == datetime(2020, 1, 1, 6, 17, 38)
    assert spec.end_time.datetime == datetime(2020, 1, 1, 15, 27, 43)
    assert spec.wavelength.min == 25000 * u.kHz
    assert spec.wavelength.max == 180000 * u.kHz