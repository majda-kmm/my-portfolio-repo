import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# connexion à la DB
db_user = 'admin'
db_password = 'admin'
db_host = 'localhost'
db_port = '5432'
db_name = 'cars_db'

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# on lit les données de la table car_reviews 
query = "SELECT * FROM car_reviews;"
df = pd.read_sql(query, engine)

# on "normalise" les types de moteur
df['Engine Type'] = df['Engine Type'].str.lower().str.strip()
df = df[df['Engine Type'].isin(['electric', 'thermal'])]  # filter valeurs valides only

# groupby volume par année
volume = df.groupby(['Review Year', 'Engine Type'])['Sales Volume'].sum().unstack().fillna(0)

# plot volume
volume.plot(kind='bar', stacked=True,color=['#4018E3', '#d62728'])
plt.title('Volume of electric vs thermal cars sold per year')
plt.xlabel('Year')
plt.ylabel('Sales volume')
plt.legend(title='Engine type')
plt.tight_layout()
plt.savefig('volume_per_year.png')
plt.show()

# groupby valeur par année
df['Value'] = df['Sales Volume'] * df['Price']
value = df.groupby(['Review Year', 'Engine Type'])['Value'].sum().unstack().fillna(0)

# plot valeur
value.plot(kind='bar', stacked=True,color=['#4018E3', '#d62728'])
plt.title('Value of electric vs thermal cars sold per year')
plt.xlabel('Year')
plt.ylabel('Total value (price × volume)')
plt.legend(title='Engine type')
plt.tight_layout()
plt.savefig('value_per_year.png')
plt.show()