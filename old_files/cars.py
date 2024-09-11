car_models = [
    'Tesla Model S', 'Ford Mustang', 'Chevrolet Camaro', 'BMW i8', 'Audi R8',
    'Porsche 911', 'Mercedes-Benz S-Class', 'Honda Civic', 'Toyota Corolla', 
    'Nissan GT-R', 'Lamborghini Aventador', 'Ferrari 488', 'McLaren 720S', 
    'Aston Martin DB11', 'Jaguar F-Type', 'Lexus LC', 'Kia Stinger', 'Hyundai Genesis',
    'Mazda MX-5 Miata', 'Subaru WRX', 'Dodge Challenger', 'Volkswagen Golf', 'Mini Cooper', 
    'Volvo XC90', 'Range Rover Sport', 'Tesla Model X', 'Chevrolet Tahoe', 'Ford F-150', 
    'Toyota Tundra', 'GMC Sierra', 'Ram 1500', 'Jeep Wrangler', 'Chevrolet Suburban',
    'Cadillac Escalade', 'BMW X5', 'Audi Q7', 'Porsche Cayenne', 'Lexus RX', 'Honda CR-V', 
    'Toyota RAV4', 'Nissan Rogue', 'Hyundai Tucson', 'Ford Explorer', 'Jeep Grand Cherokee', 
    'Mazda CX-5', 'Subaru Outback', 'Tesla Model 3', 'Hyundai Ioniq 5', 'Rivian R1T',
    'Lucid Air'
]

descriptions = [
    'A luxury electric sedan with advanced autonomous driving features.',
    'A classic American muscle car with a strong V8 engine and sporty design.',
    'A high-performance sports car known for its aggressive styling and power.',
    'A hybrid sports car with futuristic design and eco-friendly technology.',
    'A mid-engine supercar with exceptional performance and handling.',
    'A timeless sports car with a rear-engine design and iconic silhouette.',
    'A flagship luxury sedan with top-tier comfort, technology, and safety.',
    'A popular compact sedan with reliable performance and efficiency.',
    'A well-rounded compact sedan known for its reliability and fuel economy.',
    'A high-performance sports car with all-wheel drive and powerful engine.',
    'An exotic supercar with a V12 engine and striking design.',
    'A mid-engine supercar with incredible speed and precision handling.',
    'A lightweight, high-performance sports car with a twin-turbo V8 engine.',
    'A grand tourer that combines luxury, performance, and British craftsmanship.',
    'A sleek and powerful sports car with British engineering.',
    'A luxurious coupe with a focus on performance and design.',
    'A sporty sedan with a turbocharged engine and sharp handling.',
    'A luxury sedan offering refined performance and a premium interior.',
    'A lightweight convertible with nimble handling and fun driving dynamics.',
    'A high-performance sedan with turbocharged engines and rally-inspired design.',
    'A retro-styled muscle car with a powerful engine lineup.',
    'A compact hatchback offering a blend of performance and practicality.',
    'A small, quirky car with a fun-to-drive character.',
    'A luxury SUV known for its safety, technology, and spaciousness.',
    'A high-performance SUV with off-road capabilities and luxury amenities.',
    'An electric SUV with impressive range and futuristic features.',
    'A large SUV with a focus on space, towing capacity, and comfort.',
    'A best-selling full-size truck with a variety of powerful engine options.',
    'A rugged full-size pickup truck known for its durability and power.',
    'A full-size pickup truck with a focus on power and technology.',
    'A robust and capable pickup truck with off-road features.',
    'A rugged SUV with off-road capabilities and a loyal fanbase.',
    'A large SUV designed for families with ample cargo space.',
    'A luxury SUV offering power, space, and top-tier amenities.',
    'A midsize luxury SUV with a focus on performance and comfort.',
    'A luxury SUV with advanced technology and powerful engine options.',
    'A sporty midsize SUV with a strong V6 engine and agile handling.',
    'A reliable compact SUV known for its safety and practicality.',
    'A popular compact SUV with good fuel efficiency and practicality.',
    'A compact SUV with modern styling and a comfortable interior.',
    'A reliable compact SUV with advanced safety features and good value.',
    'A midsize SUV offering a blend of space, performance, and comfort.',
    'A rugged SUV with off-road capabilities and a premium interior.',
    'A compact SUV offering a good balance of performance and comfort.',
    'A rugged wagon with all-wheel drive and outdoor-oriented features.',
    'An electric sedan offering long range and cutting-edge technology.',
    'A futuristic electric crossover with advanced technology and range.',
    'An electric pickup truck with impressive performance and range.',
    'A luxury electric sedan with a focus on range and cutting-edge technology.',
    'A stylish electric sedan with modern design and premium features.'
]

# Ensure the lengths are the same
if len(car_models) == len(descriptions):
    print("Lengths match:", len(car_models))
else:
    print(f"Lengths mismatch: {len(car_models)} models, {len(descriptions)} descriptions")

# Then convert to DataFrame and CSV
import pandas as pd

data = {
    'Car Model': car_models,
    'Description': descriptions
}

df = pd.DataFrame(data)
df.to_csv('cars_data.csv', index=False)

print("CSV file created successfully.")
