import numpy as np
numbers_of_resident = 100_000
chieu_cao = np.random.normal(loc=170, scale=5, size=numbers_of_resident)

can_duoi = 170 - 5
can_tren = 170 + 5
mat_na = (chieu_cao >= can_duoi) & (chieu_cao <= can_tren)
so_nguoi = np.sum(mat_na)
ty_le = (so_nguoi / numbers_of_resident) * 100
print("Tile of resident height between 165 and 175: " + str(ty_le))