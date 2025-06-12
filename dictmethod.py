movies_db2025 = {}
casting = ["Sunny Deol","Randeep Hooda","Saiyami Kher","Vineet Kumar Singh","Regina Cassandra"]
name = "Jaat"
movies_db2025[name] = casting
casting1 =["Akshay Kumar","Arshad Warsi"]
name = "Phule"
movies_db2025[name] = casting1
casting2 = ["Akshay Kumar","Arshad Warsi","Saurabh Shukla"]
name = "Jolly LLB 3"
movies_db2025[name] = casting2
casting3 = ["Rajkummar Rao","Wamiqa Gabbi"]
name ="Bhool Chuk Maaf"
movies_db2025[name] = casting3
(movies_db2025)

movies_db2024 = {}
casting = ["Akshay Kumar", "Tiger Shroff","Prithviraj Sukumaran","Manushi Chhillar","Alaya F","Ronit Roy"]
name = "Bade Miyab Chote Miyan"
movies_db2024[name] = casting
casting1 = ["Kartik Aaryan","Vidya Balan","Madhuri Dixit","TRiptii Dimri"]
name = "Bhool Bhulaiyaa 3"
movies_db2024[name] = casting1
casting2 = ["Ajay Devgn","R. Madhavan","Jyothika","Janki Bodiwala","Anngad Raaj"]
name = "Shaitaan"
movies_db2024[name] = casting2
casting3 = ["Hrithik Roshan","DEepika Pandukone","Anil Kapoor"]
name = "Fighter"
movies_db2024[name] = casting3
print(movies_db2024)

movies_db2023 = {}
casting = ["Shah Rukh Khan","Deepika Padukone","John Abraham","Dimple KApadia"]
name = "Pathaan"
movies_db2023[name] = casting
casting1 = ["Shah Rukh Khan","Nayanthara","Vijay Sethupathi","Deepika Padukone"]
name = "Jawan"
movies_db2023[name] = casting1
casting2 = ["Sunny Deol","Ameesha Patel","Utkarsh Sharma","Simrat Kaur"]
name = "Gadar 2"
movies_db2023[name] = casting2
casting3 = ["Kareena Kapoor Khan","Jaideep Ahlawat","Vijay Varma"]
name = "Jaane Jaan"
movies_db2023[name] = casting3
print(movies_db2023)

movies_db2022 = {}
casting = ["Ranbir Kapoor","Alia Bhatt","Amitabh Bachchan","Mouni Roy","Nagarjuna","Shah Rukh Khan"]
name = "Brahmastra: Part One - Shiva"
movies_db2022[name] = casting
casting1 = ["Ajay Devgn","Tabu","Akshaye Khanna","Shriya Saran","Ishita Dutta","Mrunal Jadhav","Rajat Kapoor"]
name = "Drishyam 2"
movies_db2022[name] = casting1
casting2 = ["Hrithik Roshan","Saif Ali Khan","Radhika Apte"]
name = "Vikram Vedha"
movies_db2022[name] = casting2
casting3 = ["John Abraham","Arjun Kapoor","Disha Patani","Tara Sutaria"]
name = "Ek Villain REturns"
movies_db2022[name] = casting3
print(movies_db2022)

bigdb = {}
bigdb = { 2022 : movies_db2022, 2023 : movies_db2023 , 2024 : movies_db2024, 2025 : movies_db2025}
print(bigdb)

for k,v in bigdb.items():
    print(k,"------->",v)

ak_count = 0
for year,movies in bigdb.items():
       print(f"\nYear : {year}")
       for movies, casting in movies.items():
        print(f" Movies : {movies}")
        print(f" Casting : {casting}")
        if "Akshay Kumar" in casting:
            ak_count += 1
            print((f"\nTotal  movies with Akshay Kumar: {ak_count}"))

