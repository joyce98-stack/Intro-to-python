# for loop
# while

# for nums in range(1,100):
#     print(nums)

# num = 0
# while num <= 10:
#     print(num)
#     num += 1  #num = num + 1


# scores=[98,65,79,55,32,91,38,52,87]
# for s in scores:
#     if (s >=50 and s<=70) or s>90:
#         print(s)

people = [
	{
		"name": "Lane Puckett",
		"email": "dictum.cursus@protonmail.org",
		"country": "Germany",
		"age": 65
	},
	{
		"name": "Lucy Stephenson",
		"email": "non.egestas@icloud.com",
		"country": "Austria",
		"age": 54
	},
	{
		"name": "Chantale Mendoza",
		"email": "tincidunt.neque.vitae@aol.net",
		"country": "Colombia",
		"age": 39
	},
	{
		"name": "Odette Little",
		"email": "arcu.vestibulum.ante@aol.edu",
		"country": "Sweden",
		"age": 19
	},
	{
		"name": "Colby Snow",
		"email": "viverra@yahoo.com",
		"country": "Australia",
		"age": 32
	},
	{
		"name": "Abbot Peterson",
		"email": "a.neque.nullam@google.org",
		"country": "South Africa",
		"age": 49
	},
	{
		"name": "Judah Eaton",
		"email": "eget.mollis.lectus@outlook.org",
		"country": "Pakistan",
		"age": 48
	},
	{
		"name": "Frances Baldwin",
		"email": "nunc.lectus.pede@yahoo.net",
		"country": "Chile",
		"age": 55
	},
	{
		"name": "Claudia Jackson",
		"email": "sit.amet.lorem@hotmail.net",
		"country": "Brazil",
		"age": 19
	},
	{
		"name": "Phelan Vaughan",
		"email": "leo.cras@icloud.ca",
		"country": "Peru",
		"age": 57
	},
	{
		"name": "Francis O'Neill",
		"email": "lacus.quisque@aol.couk",
		"country": "Vietnam",
		"age": 68
	},
	{
		"name": "Denton Vinson",
		"email": "adipiscing@outlook.edu",
		"country": "Singapore",
		"age": 43
	},
	{
		"name": "Tasha Leon",
		"email": "sed@icloud.couk",
		"country": "Singapore",
		"age": 39
	},
	{
		"name": "Adria Bright",
		"email": "dolor.vitae@outlook.org",
		"country": "Canada",
		"age": 70
	},
	{
		"name": "Dacey Faulkner",
		"email": "nulla.integer@outlook.couk",
		"country": "Austria",
		"age": 29
	},
	{
		"name": "Sade Rhodes",
		"email": "turpis.aliquam@outlook.couk",
		"country": "Russian Federation",
		"age": 23
	},
	{
		"name": "Lionel Bernard",
		"email": "ut.semper@protonmail.couk",
		"country": "France",
		"age": 42
	},
	{
		"name": "Stephanie Griffin",
		"email": "non.lobortis.quis@aol.net",
		"country": "Peru",
		"age": 43
	},
	{
		"name": "Erasmus Adkins",
		"email": "gravida@outlook.ca",
		"country": "France",
		"age": 55
	},
	{
		"name": "Abel Holman",
		"email": "ligula.aenean@icloud.org",
		"country": "Belgium",
		"age": 47
	},
	{
		"name": "Carter Alford",
		"email": "libero.morbi.accumsan@aol.couk",
		"country": "Netherlands",
		"age": 36
	},
	{
		"name": "Kareem Dejesus",
		"email": "ante.dictum.cursus@protonmail.org",
		"country": "Costa Rica",
		"age": 61
	},
	{
		"name": "Timon Parks",
		"email": "metus.vitae.velit@hotmail.couk",
		"country": "Canada",
		"age": 24
	},
	{
		"name": "Kerry Christian",
		"email": "dis.parturient.montes@outlook.couk",
		"country": "India",
		"age": 36
	},
	{
		"name": "Odette Chase",
		"email": "massa.quisque.porttitor@google.edu",
		"country": "Sweden",
		"age": 21
	},
	{
		"name": "Flynn Gray",
		"email": "nibh.aliquam@protonmail.com",
		"country": "Pakistan",
		"age": 63
	},
	{
		"name": "Mikayla Lindsay",
		"email": "tempus.scelerisque.lorem@outlook.edu",
		"country": "Sweden",
		"age": 36
	},
	{
		"name": "Florence Gilbert",
		"email": "magnis.dis.parturient@google.couk",
		"country": "United Kingdom",
		"age": 52
	},
	{
		"name": "Odette Key",
		"email": "lorem.ipsum.dolor@google.net",
		"country": "Poland",
		"age": 37
	},
	{
		"name": "Barrett Valencia",
		"email": "sed.eu@outlook.net",
		"country": "Sweden",
		"age": 45
	},
	{
		"name": "Jermaine Salinas",
		"email": "risus.morbi.metus@icloud.net",
		"country": "Vietnam",
		"age": 16
	},
	{
		"name": "Tatiana Dalton",
		"email": "vel.arcu@icloud.edu",
		"country": "Singapore",
		"age": 19
	},
	{
		"name": "Arthur Ware",
		"email": "mi.felis@protonmail.net",
		"country": "India",
		"age": 49
	},
	{
		"name": "Winifred Hatfield",
		"email": "maecenas.iaculis.aliquet@hotmail.ca",
		"country": "Norway",
		"age": 53
	},
	{
		"name": "Zachery Horn",
		"email": "mauris.rhoncus@protonmail.couk",
		"country": "Norway",
		"age": 49
	},
	{
		"name": "Basia Turner",
		"email": "aliquam.arcu.aliquam@aol.edu",
		"country": "Belgium",
		"age": 57
	},
	{
		"name": "Pascale Little",
		"email": "sed@yahoo.com",
		"country": "Brazil",
		"age": 31
	},
	{
		"name": "Alexa Rojas",
		"email": "imperdiet.erat.nonummy@google.couk",
		"country": "Nigeria",
		"age": 62
	},
	{
		"name": "Caryn Rosario",
		"email": "a.facilisis.non@outlook.ca",
		"country": "Ireland",
		"age": 56
	},
	{
		"name": "Skyler Cantu",
		"email": "a.enim.suspendisse@aol.net",
		"country": "Germany",
		"age": 54
	},
	{
		"name": "Warren Valentine",
		"email": "quis.urna.nunc@protonmail.edu",
		"country": "Austria",
		"age": 39
	},
	{
		"name": "Asher Stephens",
		"email": "metus@google.org",
		"country": "Mexico",
		"age": 18
	},
	{
		"name": "Perry Day",
		"email": "ultricies.dignissim@google.org",
		"country": "Ireland",
		"age": 41
	},
	{
		"name": "Brianna Hunter",
		"email": "elit.dictum@yahoo.org",
		"country": "United Kingdom",
		"age": 37
	},
	{
		"name": "Keegan Thompson",
		"email": "cras@aol.couk",
		"country": "Turkey",
		"age": 19
	},
	{
		"name": "Farrah Waters",
		"email": "auctor.vitae@yahoo.edu",
		"country": "Sweden",
		"age": 62
	},
	{
		"name": "Brent Morin",
		"email": "velit.egestas@aol.org",
		"country": "Ukraine",
		"age": 24
	},
	{
		"name": "Luke Johnson",
		"email": "blandit.at@outlook.edu",
		"country": "Germany",
		"age": 32
	},
	{
		"name": "Harriet Beasley",
		"email": "vitae.posuere.at@protonmail.net",
		"country": "Philippines",
		"age": 68
	},
	{
		"name": "Montana Snow",
		"email": "elit.curabitur@protonmail.org",
		"country": "Austria",
		"age": 70
	},
	{
		"name": "Jessamine Sosa",
		"email": "nisi@outlook.ca",
		"country": "Nigeria",
		"age": 27
	},
	{
		"name": "Merritt Haney",
		"email": "cursus.et.magna@outlook.net",
		"country": "Germany",
		"age": 55
	},
	{
		"name": "Lysandra Barnett",
		"email": "rhoncus@protonmail.net",
		"country": "France",
		"age": 33
	},
	{
		"name": "Julie Dotson",
		"email": "vel@outlook.edu",
		"country": "Australia",
		"age": 52
	},
	{
		"name": "Murphy Richmond",
		"email": "ullamcorper.nisl.arcu@outlook.org",
		"country": "Brazil",
		"age": 55
	},
	{
		"name": "Jack Cote",
		"email": "vivamus@yahoo.edu",
		"country": "United States",
		"age": 30
	},
	{
		"name": "Deirdre Graham",
		"email": "sociosqu.ad.litora@yahoo.com",
		"country": "Philippines",
		"age": 45
	},
	{
		"name": "Hilel Oneil",
		"email": "eu.tempor@protonmail.edu",
		"country": "Colombia",
		"age": 38
	},
	{
		"name": "Keefe Gardner",
		"email": "metus@yahoo.org",
		"country": "Belgium",
		"age": 20
	},
	{
		"name": "Jael Copeland",
		"email": "habitant@hotmail.couk",
		"country": "Netherlands",
		"age": 37
	},
	{
		"name": "Kyle Griffin",
		"email": "aliquam.eu.accumsan@icloud.ca",
		"country": "Peru",
		"age": 26
	},
	{
		"name": "Magee Landry",
		"email": "a.purus.duis@google.couk",
		"country": "Italy",
		"age": 56
	},
	{
		"name": "Bruno Park",
		"email": "vel.nisl.quisque@hotmail.com",
		"country": "Vietnam",
		"age": 35
	},
	{
		"name": "Orla Yates",
		"email": "condimentum@hotmail.net",
		"country": "Philippines",
		"age": 69
	},
	{
		"name": "Quynn Diaz",
		"email": "facilisis.eget@google.org",
		"country": "South Korea",
		"age": 40
	},
	{
		"name": "Brooke Lynch",
		"email": "nascetur.ridiculus.mus@protonmail.couk",
		"country": "Spain",
		"age": 46
	},
	{
		"name": "Thomas Jones",
		"email": "vivamus.non@yahoo.com",
		"country": "South Africa",
		"age": 28
	},
	{
		"name": "Brennan Carpenter",
		"email": "felis@outlook.com",
		"country": "Nigeria",
		"age": 30
	},
	{
		"name": "Yoko Cochran",
		"email": "nibh.phasellus.nulla@protonmail.net",
		"country": "Costa Rica",
		"age": 27
	},
	{
		"name": "Isaiah Warner",
		"email": "donec.tempor@outlook.ca",
		"country": "Pakistan",
		"age": 32
	},
	{
		"name": "Drake Ellison",
		"email": "est.mauris@hotmail.com",
		"country": "New Zealand",
		"age": 60
	},
	{
		"name": "Leigh Simpson",
		"email": "lorem@icloud.couk",
		"country": "Mexico",
		"age": 19
	},
	{
		"name": "Cedric Estrada",
		"email": "ornare.fusce@hotmail.ca",
		"country": "India",
		"age": 44
	},
	{
		"name": "Stacy Chase",
		"email": "lectus.convallis@outlook.edu",
		"country": "France",
		"age": 20
	},
	{
		"name": "Christine Kinney",
		"email": "dolor.tempus@hotmail.com",
		"country": "Canada",
		"age": 43
	},
	{
		"name": "Driscoll Arnold",
		"email": "ac.turpis@icloud.com",
		"country": "United Kingdom",
		"age": 40
	},
	{
		"name": "Lucius Bruce",
		"email": "quam@icloud.org",
		"country": "Germany",
		"age": 34
	},
	{
		"name": "Stacey Wood",
		"email": "nunc@google.org",
		"country": "China",
		"age": 24
	},
	{
		"name": "Fay Allen",
		"email": "facilisis@hotmail.com",
		"country": "Austria",
		"age": 47
	},
	{
		"name": "Teegan Barron",
		"email": "eu@icloud.org",
		"country": "Colombia",
		"age": 42
	},
	{
		"name": "Luke Hays",
		"email": "accumsan.neque@yahoo.couk",
		"country": "Brazil",
		"age": 16
	},
	{
		"name": "Brendan Wiley",
		"email": "senectus@hotmail.net",
		"country": "Pakistan",
		"age": 48
	},
	{
		"name": "Calista Dudley",
		"email": "curabitur@hotmail.org",
		"country": "Australia",
		"age": 36
	},
	{
		"name": "Nelle Klein",
		"email": "quam.quis@hotmail.edu",
		"country": "Brazil",
		"age": 24
	},
	{
		"name": "Cain Hendricks",
		"email": "donec.vitae.erat@protonmail.edu",
		"country": "Belgium",
		"age": 63
	},
	{
		"name": "Beverly Melton",
		"email": "sit.amet.dapibus@protonmail.net",
		"country": "Netherlands",
		"age": 56
	},
	{
		"name": "Laith Talley",
		"email": "maecenas@aol.edu",
		"country": "Colombia",
		"age": 40
	},
	{
		"name": "Jaden Moss",
		"email": "aliquet.metus@yahoo.edu",
		"country": "Austria",
		"age": 61
	},
	{
		"name": "Beatrice Duke",
		"email": "a.odio@icloud.com",
		"country": "Netherlands",
		"age": 59
	},
	{
		"name": "Jerome Nash",
		"email": "ante.ipsum.primis@icloud.ca",
		"country": "Peru",
		"age": 33
	},
	{
		"name": "Barbara Guy",
		"email": "laoreet@hotmail.net",
		"country": "China",
		"age": 40
	},
	{
		"name": "Ingrid Harrington",
		"email": "vel.quam@outlook.org",
		"country": "United Kingdom",
		"age": 24
	},
	{
		"name": "Omar Hartman",
		"email": "tristique.pellentesque.tellus@outlook.net",
		"country": "Poland",
		"age": 22
	},
	{
		"name": "Georgia Powell",
		"email": "nullam.velit.dui@outlook.net",
		"country": "United Kingdom",
		"age": 55
	},
	{
		"name": "Ella Coleman",
		"email": "mi.ac@hotmail.ca",
		"country": "Norway",
		"age": 45
	},
	{
		"name": "Talon Campos",
		"email": "non.lacinia.at@protonmail.org",
		"country": "Ukraine",
		"age": 24
	},
	{
		"name": "Abbot Levy",
		"email": "nec.euismod@protonmail.couk",
		"country": "Sweden",
		"age": 29
	},
	{
		"name": "Yuli Valencia",
		"email": "sed.dictum@protonmail.edu",
		"country": "Poland",
		"age": 43
	},
	{
		"name": "Destiny Blair",
		"email": "adipiscing.lobortis@icloud.com",
		"country": "Italy",
		"age": 51
	},
	{
		"name": "Deanna Sargent",
		"email": "tellus@google.ca",
		"country": "Nigeria",
		"age": 24
	}
]

# print details
for person in people:
    name = person["name"]
    age = person["age"]
    country = person["country"]
    if country == "Italy"and age>55:
       print(f"Name is {name} Age is {age} Country is {country}")

# TODO sort by age



