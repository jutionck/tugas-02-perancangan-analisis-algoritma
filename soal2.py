def calculateDuration(departureTime, arrivalTime):
    departureSeconds = departureTime[0] * 3600 + departureTime[1] * 60 + departureTime[2]

    arrivalSeconds = arrivalTime[0] * 3600 + arrivalTime[1] * 60 + arrivalTime[2]

    durationSeconds = arrivalSeconds - departureSeconds

    durationHours = durationSeconds // 3600
    durationMinutes = (durationSeconds % 3600) // 60
    durationSeconds = durationSeconds % 60

    output = f"Waktu perjalanan: {durationHours} jam, {durationMinutes} menit, {durationSeconds} detik"
    return output

departureTmeInput = input("Masukkan waktu keberangkatan (HH:MM:SS): ")
departureTime = tuple(map(int, departureTmeInput.split(":")))

arrivalTimeInput = input("Masukkan waktu kedatangan (HH:MM:SS): ")
arrivalTime = tuple(map(int, arrivalTimeInput.split(":")))

output = calculateDuration(departureTime, arrivalTime)

print(output)
