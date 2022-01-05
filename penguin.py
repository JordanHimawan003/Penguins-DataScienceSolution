# %% [markdown]
# # Import Package

# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %% [markdown]
# # Data Preparation

# %%
# import dataset
penguin = pd.read_csv('./dataset/penguins.csv')
penguin

# %%
# cek presentase data kosong
penguin.isna().sum() / penguin.shape[0] * 100

# %% [markdown]
# # Data Preprocessing

# %%
# duplikasi data mentah ke data olah
penguin_olah = penguin.copy()

# menghapus data kosong
penguin_olah = penguin_olah.dropna()

#  cek ulang presentase data kosong
penguin_olah.isna().sum() / penguin.shape[0] * 100

# %%
# cek jumlah value unik untuk melihat data aneh
penguin_olah.nunique()

# mencari data aneh
penguin_olah['sex'].unique()

# %%
# fix data aneh
penguin_olah['sex'].loc[penguin_olah['sex'] == '.'] = penguin_olah['sex'].mode()[0]

# %% [markdown]
# # Visualisasi

# %%
# menampilkan data penguin menggunakan histogram
for x in penguin_olah.columns:
  plt.hist(penguin_olah[x])
  plt.title(x)
  plt.show()

# %%
# visualisasi spesies berdasarkan panjang paruh dan kedalaman paruh
sns.jointplot(data=penguin_olah, x='culmen_length_mm', y='culmen_depth_mm', hue='species')

# %%
# menampilkan hubungan jenis kelamin dengan panjang paruh dan berat badan
sns.scatterplot(data = penguin_olah, x='culmen_length_mm', y='body_mass_g', hue='sex')

# %%
# menampilkan seluruh perbandingan data penguin
sns.pairplot(penguin_olah, hue = 'species', height = 2)


