# Create function
def calculateArrivalTime(hours, minutes, seconds, duration):
    departureTimeSeconds = hours * 3600 + minutes * 60 + seconds
    totalTimeSeconds = departureTimeSeconds + duration
    arrivalHours = totalTimeSeconds // 3600
    totalTimeSeconds %= 3600
    arrivalMinutes = totalTimeSeconds // 60
    arrivalSeconds = totalTimeSeconds % 60
    arrivalTime = f"Waktu kedatangan pukul: {arrivalHours:02d}:{arrivalMinutes:02d}:{arrivalSeconds:02d}"
    return arrivalTime

# Demo Apps
departureHours = int(input("Masukkan jam: "))
departureMinutes = int(input("Masukkan menit: "))
departureSeconds = int(input("Masukan detik: "))

# Input for travel duration
travelDurationSeconds = int(input("Tentukan durasi perjalanan (dalam detik): "))

arrivalTime = calculateArrivalTime(departureHours, departureMinutes, departureSeconds, travelDurationSeconds)

print(arrivalTime)