import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

views = ad_clicks.groupby('utm_source').user_id.count().reset_index()

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()

#percentage = True / (True + False)
clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])

clicks_by_groups = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
clicks_by_group_pivot = clicks_by_groups.pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id'
).reset_index()

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
 
a_clicks_pivot = a_clicks\
  .groupby(['day','is_click']).user_id\
  .count().reset_index()\
  .pivot(
    columns = 'is_click',
    index = 'day',
    values = 'user_id'
  ).reset_index()  #pivot可以直接跟在前一个后面写；转换成pivot table后再计算percentage

a_clicks_pivot['percent_click'] = a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])
print(a_clicks_pivot)

b_clicks_pivot = b_clicks\
  .groupby(['day','is_click']).user_id\
  .count().reset_index()\
  .pivot(
    columns = 'is_click',
    index = 'day',
    values = 'user_id'
  ).reset_index()

b_clicks_pivot['percent_click'] = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])
print(b_clicks_pivot)

print(clicks_by_group_pivot)
