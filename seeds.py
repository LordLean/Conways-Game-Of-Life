# Glider
seed_glider = [(2,2),(3,3),(4,1),(4,2),(4,3)]

# Penta-decathlon
seed_penta_decathlon = [(8,15),
(9,15),
(10,14),(10,15),(10,16),
(13,14),(13,15),(13,16),
(14,15),
(15,15),
(16,15),
(17,15),
(18,14),(18,15),(18,16),
(21,14),(21,15),(21,16),
(22,15),
(23,15)
]

# Methuselah: R-pentomino
seed_r_pentomino = [(15,15),(15,16),
(16,14),(16,15),
(17,15)]

# Fun
seed_fun = [(20,17),(20,18),(20,19),
(21,17),(21,19),
(22,17),(22,19),
(23,17),(23,18),(23,19),
(24,17),(24,18),(24,19)
]

# New Seed
seed_new = []

# Add new seeds here. 
# {CLI Key: [<name>, <seed's list of tuples>]}
seed_collection = {
    -1: ["Random", []],
    0 : ["Glider", seed_glider],
    1 : ["Penta Decathlon", seed_penta_decathlon],
    2 : ["R Pentomino", seed_r_pentomino],
    3 : ["Fun", seed_fun]
}