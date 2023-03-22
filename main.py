# -*- coding: utf-8 -*-
# Author: Oren Sternberg
# Date: 3/22/2023
# Description: EnviromentalAcousticalNoiseModels DRAFT
# GitHub: https://github.com/0r3ntal

import numpy as np
import matplotlib.pyplot as plt

class EnvironmentalAcoustics:

    def __init__(self):
        pass

    def traffic_noise_tnm(self, distance, traffic_volume, speed, road_type):
        """
        Calculate traffic noise based on distance, traffic volume, speed, and road type using a simplified version
        of the Federal Highway Administration (FHWA) Traffic Noise Model (TNM).

        :param distance: Distance from the road to the receiver in meters.
        :param traffic_volume: Average traffic volume per hour (vehicles per hour).
        :param speed: Average speed of vehicles in km/h.
        :param road_type: Road surface type as a string: "light", "medium", or "heavy".
        :return: A-weighted sound level in dB(A).
        """
        # Constants for road type adjustments
        road_type_adjustments = {
            'light': 0,
            'medium': 2,
            'heavy': 4
        }

        # Check if the road type is valid
        if road_type not in road_type_adjustments:
            raise ValueError('Invalid road type. Choose from "light", "medium", or "heavy".')

        # Calculate traffic noise using the simplified TNM
        reference_distance = 15  # Reference distance in meters
        absorption_coefficient = 0.005  # Absorption coefficient (typical value for open terrain)

        # Calculate base noise level
        base_noise_level = 50 + 10 * np.log10(traffic_volume) + 10 * np.log10(speed)

        # Apply road noise adjustment
        road_noise_adjustment = road_type_adjustments[road_type]

        # Calculate distance attenuation
        distance_attenuation = 20 * np.log10(distance / reference_distance)

        # Calculate atmospheric absorption
        atmospheric_absorption = absorption_coefficient * distance

        # Calculate final noise level
        noise_level = base_noise_level + road_noise_adjustment - distance_attenuation - atmospheric_absorption

        # Return noise level
        return noise_level

    def traffic_noise_crtn(self, distance, traffic_volume, speed, road_type):
        """
        Calculate traffic noise based on distance, traffic volume, speed, and road type using the Calculation of
        Road Traffic Noise (CRTN) model.

        :param distance: Distance from the road to the receiver in meters.
        :param traffic_volume: Average traffic volume per hour (vehicles per hour).
        :param speed: Average speed of vehicles in km/h.
        :param road_type: Road surface type as a string: "light", "medium", or "heavy".
        :return: A-weighted sound level in dB(A).
        """
        # Constants for road type adjustments
        road_type_adjustments = {
            'light': 0,
            'medium': 2,
            'heavy': 4
        }

        # Check if the road type is valid
        if road_type not in road_type_adjustments:
            raise ValueError('Invalid road type. Choose from "light", "medium", or "heavy".')

        # Calculate traffic noise using the CRTN model
        reference_distance = 10  # Reference distance in meters

        # Calculate base noise level
        base_noise_level = 68 + 10 * np.log10(traffic_volume) + 10 * np.log10(speed)

        # Apply road noise adjustment
        road_noise_adjustment = road_type_adjustments[road_type]

        # Calculate distance attenuation
        distance_attenuation = 20 * np.log10(distance / reference_distance)

        # Ground absorption coefficient (assumed for soft ground)
        ground_absorption = -1.5

        # Calculate final noise level
        noise_level = base_noise_level + road_noise_adjustment - distance_attenuation + ground_absorption

        # Return noise level
        return noise_level

    def railway_noise(self, distance, train_volume, speed, track_type):
        """
        Calculate railway noise based on distance, train volume, speed, and track type.

        :param distance: Distance from the railway to the receiver in meters.
        :param train_volume: Number of trains per hour.
        :param speed: Average speed of trains in km/h.
        :param track_type: Track type as a string: "light", "medium", or "heavy".
        :return: A-weighted sound level in dB(A).
        """
        # Constants and adjustments for track type
        track_type_adjustments = {
            'light': 0,
            'medium': 2,
            'heavy': 4
        }

        if track_type not in track_type_adjustments:
            raise ValueError('Invalid track type. Choose from "light", "medium", or "heavy".')

        reference_distance = 10
        base_noise_level = 68 + 10 * np.log10(train_volume) + 10 * np.log10(speed)
        track_noise_adjustment = track_type_adjustments[track_type]
        distance_attenuation = 20 * np.log10(distance / reference_distance)

        noise_level = base_noise_level + track_noise_adjustment - distance_attenuation
        return noise_level

    def aircraft_noise(self, distance, flight_volume, aircraft_type, flight_path):
        """
        Calculate aircraft noise based on distance, flight volume, aircraft type, and flight path.

        :param distance: Distance from the aircraft to the receiver in meters.
        :param flight_volume: Number of flights per hour.
        :param aircraft_type: Aircraft type as a string (e.g., "small_prop", "large_prop", "jet").
        :param flight_path: Flight path as a string (e.g., "landing", "takeoff", "cruise").
        :return: A-weighted sound level in dB(A).
        """
        # Constants and adjustments for aircraft type and flight path
        # These are hypothetical adjustments and might need modification based on real data or standards
        aircraft_type_adjustments = {
            'small_prop': -10,
            'large_prop': 0,
            'jet': 10
        }

        flight_path_adjustments = {
            'landing': -5,
            'takeoff': 0,
            'cruise': -15
        }

        if aircraft_type not in aircraft_type_adjustments:
            raise ValueError('Invalid aircraft type. Choose from "small_prop", "large_prop", or "jet".')

        if flight_path not in flight_path_adjustments:
            raise ValueError('Invalid flight path. Choose from "landing", "takeoff", or "cruise".')

        reference_distance = 1000
        base_noise_level = 80 + 10 * np.log10(flight_volume)
        aircraft_noise_adjustment = aircraft_type_adjustments[aircraft_type]
        flight_path_noise_adjustment = flight_path_adjustments[flight_path]
        distance_attenuation = 20 * np.log10(distance / reference_distance)

        noise_level = base_noise_level + aircraft_noise_adjustment + flight_path_noise_adjustment - distance_attenuation
        return noise_level

    def industrial_noise(self, distance, source_level, source_type, terrain):
        """
        Calculate industrial noise based on distance, source level, source type, and terrain.

       :param distance: Distance from the industrial source to the receiver in meters.
       :param source_level: Noise level of the industrial source in dB(A).
       :param source_type: Source type as a string (e.g., "factory", "power_plant", "construction").
       :param terrain: Terrain as a string (e.g., "urban", "suburban", "rural").
       :return: A-weighted sound level in dB(A).
        """

    # Constants and adjustments for source type and terrain
    # These are hypothetical adjustments and might need modification based on real data or standards
        source_type_adjustments = {
            'factory': 0,
            'power_plant': 5,
            'construction': 10
        }

        terrain_adjustments = {
            'urban': 0,
            'suburban': -5,
            'rural': -10
        }

        if source_type not in source_type_adjustments:
            raise ValueError('Invalid source type. Choose from "factory", "power_plant", or "construction".')

        if terrain not in terrain_adjustments:
            raise ValueError('Invalid terrain. Choose from "urban", "suburban", or "rural".')

        reference_distance = 100
        source_noise_adjustment = source_type_adjustments[source_type]
        terrain_noise_adjustment = terrain_adjustments[terrain]
        distance_attenuation = 20 * np.log10(distance / reference_distance)

        noise_level = source_level + source_noise_adjustment + terrain_noise_adjustment - distance_attenuation
        return noise_level



        pass

    def wind_turbine_noise(self, distance, turbine_power, wind_speed, terrain):
        """
        Calculate wind turbine noise based on distance, turbine power, wind_speed, and terrain.

        :param distance: Distance from the wind turbine to the receiver in meters.
        :param turbine_power: Turbine power in kW.
        :param wind_speed: Wind speed in m/s.
        :param terrain: Terrain as a string (e.g., "flat", "hilly", "mountainous").
        :return: A-weighted sound level in dB(A).
        """
        # Constants and adjustments for terrain
        # These are hypothetical adjustments and might need modification based on real data or standards
        terrain_adjustments = {
            'flat': 0,
            'hilly': -5,
            'mountainous': -10
        }

        if terrain not in terrain_adjustments:
            raise ValueError('Invalid terrain. Choose from "flat", "hilly", or "mountainous".')

        reference_distance = 100
        base_noise_level = 90 + 10 * np.log10(turbine_power) - 20 * np.log10(wind_speed)
        terrain_noise_adjustment = terrain_adjustments[terrain]
        distance_attenuation = 20 * np.log10(distance / reference_distance)

        noise_level = base_noise_level + terrain_noise_adjustment - distance_attenuation
        return noise_level


    def weighted_sound_levels(self, frequency_bands, sound_levels):
        """
        Calculate A-weighted sound levels for a given set of frequency bands and sound levels.

        :param frequency_bands: List of frequency bands in Hz.
        :param sound_levels: List of corresponding sound levels in dB.
        :return: List of A-weighted sound levels in dB(A).
        """
        a_weighting = [20.599 * np.log10(frequency) - 16.1 for frequency in frequency_bands]
        a_weighted_levels = [level + weighting for level, weighting in zip(sound_levels, a_weighting)]
        return a_weighted_levels

    def pink_noise(self, frequency):
        """
        Generate pink noise for a given frequency.

        :param frequency: Frequency in Hz.
        :return: Pink noise level in dB.
        """
        pink_noise_level = -10 * np.log10(frequency)
        return pink_noise_level

def plot_noise_levels(distances, noise_levels, title):
    plt.plot(distances, noise_levels, marker='o', linestyle='-')
    plt.xlabel('Distance (m)')
    plt.ylabel('A-weighted Sound Level (dB(A))')
    plt.title(title)
    plt.grid(True)

def plot_pink_noise_levels(frequency_bands, noise_levels, label):
    plt.plot(frequency_bands, noise_levels, label=label)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Noise Level (dB)')
    plt.title(label)
    plt.grid(True)
    plt.legend()

if __name__ == '__main__':
    ea = EnvironmentalAcoustics()

    distances = np.linspace(10, 200, 20)

    # Traffic Noise (TNM)
    traffic_volume_tnm = 500
    speed_tnm = 100
    road_type_tnm = 'heavy'
    traffic_noise_tnm_levels = [ea.traffic_noise_tnm(d, traffic_volume_tnm, speed_tnm, road_type_tnm) for d in
                                distances]

    # Traffic Noise (CRTN)
    traffic_volume_crtn = 500
    speed_crtn = 100
    road_type_crtn = 'heavy'
    traffic_noise_crtn_levels = [ea.traffic_noise_crtn(d, traffic_volume_crtn, speed_crtn, road_type_crtn) for d in
                                 distances]

    # Railway Noise
    train_volume = 10
    speed = 100
    track_type = 'medium'
    railway_noise_levels = [ea.railway_noise(d, train_volume, speed, track_type) for d in distances]

    # Aircraft Noise
    flight_volume = 5
    aircraft_type = 'jet'
    flight_path = 'landing'
    aircraft_noise_levels = [ea.aircraft_noise(d, flight_volume, aircraft_type, flight_path) for d in distances]

    # Industrial Noise
    source_level = 80
    source_type = 'factory'
    terrain = 'urban'
    industrial_noise_levels = [ea.industrial_noise(d, source_level, source_type, terrain) for d in distances]

    # Wind Turbine Noise
    turbine_power = 2000
    wind_speed = 10
    terrain = 'hilly'  # Define the terrain variable with a valid value
    wind_turbine_noise_levels = [ea.wind_turbine_noise(d, turbine_power, wind_speed, terrain) for d in distances]

    # Weighted Sound Levels
    frequency_weights = np.array([0.5, 1, 2, 4, 8, 16])
    sound_pressure_levels = np.array([60, 63, 65, 68, 70, 74])
    weighted_sound_level = ea.weighted_sound_levels(frequency_weights, sound_pressure_levels)

    # Pink Noise

    frequency_bands = np.array([31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000])

    pink_noise_levels = [ea.pink_noise(f) for f in frequency_bands]

    plt.figure(figsize=(12, 16))

    plt.subplot(4, 2, 1)
    plot_noise_levels(distances, traffic_noise_tnm_levels, 'Traffic Noise (TNM)')

    plt.subplot(4, 2, 2)
    plot_noise_levels(distances, traffic_noise_crtn_levels, 'Traffic Noise (CRTN)')

    plt.subplot(4, 2, 3)
    plot_noise_levels(distances, railway_noise_levels, 'Railway Noise')

    plt.subplot(4, 2, 4)
    plot_noise_levels(distances, aircraft_noise_levels, 'Aircraft Noise')

    plt.subplot(4, 2, 5)
    plot_noise_levels(distances, industrial_noise_levels, 'Industrial Noise')

    plt.subplot(4, 2, 6)
    plot_noise_levels(distances, wind_turbine_noise_levels, 'Wind Turbine Noise')

    plt.subplot(4, 2, 7)
    plot_pink_noise_levels(frequency_bands, pink_noise_levels, 'Pink Noise')

    plt.tight_layout()
    plt.savefig('noise_levels.png')  # Add this line to save the figure
    plt.show()