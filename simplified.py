from car_models import car_models

from descriptions import descriptions

# Step 3: Check if lengths are the same
if len(car_models) == len(descriptions):
    print("Lengths match:", len(car_models))
else:
    print(f"Lengths mismatch: {len(car_models)} models, {len(descriptions)} descriptions")

# Step 4: Create a DataFrame and save it as a CSV file
import pandas as pd

data = {
    'Car Model': car_models,
    'Description': descriptions
}

df = pd.DataFrame(data)
df.to_csv('new_cars_data.csv', index=False)

print("CSV file created successfully.")
