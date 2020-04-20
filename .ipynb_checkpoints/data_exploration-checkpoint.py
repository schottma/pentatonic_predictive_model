import pandas as pd
electronics = pd.read_csv('electronics.csv')
profiles = pd.read_csv('profile.csv')
df = pd.merge(electronics, profiles, on='clients')

binaries = ['0', '1']
df = df[df['previously_shoped'].isin(binaries)]

contingency_table_mem = pd.crosstab(electronics['member'], electronics['got_a_TV'])
contingency_table_prop_mem = contingency_table_mem.div(contingency_table_mem.sum(axis=1), axis=0)
# membership seems to have no effect on whether someone buys a TV or not

contingency_table_prev = pd.crosstab(electronics['previously_shoped'], electronics['got_a_TV'])
contingency_table_prop_prev = contingency_table_prev.div(contingency_table_prev.sum(axis=1), axis=0)
# previously_shopped seems to have no effect on whether someone buys a TV or not

contingency_table_fin = pd.crosstab(electronics['require_financing'], electronics['got_a_TV'])
contingency_table_prop_fin = contingency_table_fin.div(contingency_table_fin.sum(axis=1), axis=0)
# people that required financing were twice as likely to buy a TV

contingency_table_prom = pd.crosstab(electronics['promotion'], electronics['got_a_TV'])
contingency_table_prop_prom = contingency_table_prom.div(contingency_table_prom.sum(axis=1), axis=0)
# promotion doesn't seem to have effect on whether someone buys a TV or not

contingency_table_prize = pd.crosstab(electronics['prize_won'], electronics['got_a_TV'])
contingency_table_prop_prize = contingency_table_prize.div(contingency_table_prom.sum(axis=1), axis=0)
# seems like those who win a prize are less likely to buy a TV

contingency_table_comp = pd.crosstab(electronics['shop_competitor'], electronics['got_a_TV'])
contingency_table_prop_comp = contingency_table_comp.div(contingency_table_comp.sum(axis=1), axis=0)
# whether they went to competitor has no effect pn whether they bought a TV or not

contingency_table_sex = pd.crosstab(df['female'], df['got_a_TV'])
contingency_table_prop_sex = contingency_table_sex.div(contingency_table_sex.sum(axis=1), axis=0)
# gender has no effect on whether someone buys a TV

contingency_table_par = pd.crosstab(df['live_with_parents'], df['got_a_TV'])
contingency_table_prop_par = contingency_table_par.div(contingency_table_par.sum(axis=1), axis=0)
# lives with parent has no effect on purchase

contingency_table_edu = pd.crosstab(df['education'], df['got_a_TV'])
contingency_table_prop_edu = contingency_table_edu.div(contingency_table_edu.sum(axis=1), axis=0)
# education has no effect on purchase

contingency_table_state = pd.crosstab(df['state'], df['got_a_TV'])
contingency_table_prop_state = contingency_table_state.div(contingency_table_state.sum(axis=1), axis=0)
# state has no effect on purchase

print(df[['LT_clients', 'prize_amount', 'amount_financing', 'amount_purchase', 'age', 'monthly_spent_electronics', 'got_a_TV', 'prize_amount']].groupby('got_a_TV').mean())
# average amount financing is much higher for those who got a TV


