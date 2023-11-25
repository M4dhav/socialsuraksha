df = pd.read_csv("fusers.csv")
df1 = pd.read_csv("users.csv")
df = pd.concat([df1,df], axis=0)
df.reset_index(drop=True, inplace=True)

df = pd.read_csv("df.csv", index_col = 0)
df.reset_index(drop=True, inplace=True)

X = df.loc[:, df.columns != "dataset"]
y = df["dataset"]
y=y.astype('int')
X
columns_to_drop = [
    "created_at",
    "profile_background_image_url",
    "lang",
    "url",
    "profile_text_color",
    "profile_background_image_url_https",
    "profile_banner_url",
    "id",
    "protected",
    "verified",
    "profile_image_url_https",
    "time_zone",
    "location",
    "profile_use_background_image",
    "default_profile_image",
    "profile_image_url",
    "geo_enabled",
    "fav_number",
    "profile_link_color",
    "profile_background_color",
    "utc_offset",
    "updated",
    "name",
    "screen_name",
]

df = df.drop(columns = columns_to_drop)

mapping = {'E13': 1, 'TFP': 1, 'INT': 0, 'TWT': 0, 'FSF': 0}
df['dataset'] = df['dataset'].replace(mapping)
df['description'].fillna(0, inplace = True)
df[ 'default_profile'].fillna(0, inplace = True)
df["profile_background_tile"].fillna(0, inplace = True)
df['profile_sidebar_border_color'] = np.where(df['profile_sidebar_border_color'] == "C0DEED", 1, 0)
df['profile_sidebar_fill_color'] = np.where(df['profile_sidebar_fill_color'] == "DDEEF6", 1, 0)
df['description'] = np.where(df['description'] != 0, 1, 0)
df.to_csv("df.csv", index = False)
dl = files.download("df.csv")