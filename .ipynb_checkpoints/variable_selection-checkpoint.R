install.packages("Information", repos = "http://cran.us.r-project.org")
install.packages("tidyr", repos = "http://cran.us.r-project.org")

electronics <- read.csv(file = 'electronics.csv')
profiles <- read.csv(file = 'profile.csv')
customer_info <- merge(electronics, profiles, by='clients')

for (column in colnames(customer_info)){
  if (!(column == "got_a_TV" )){
    customer_info[[column]] <- factor(customer_info[[column]])
  }
}

IV <- Information::create_infotables(data=customer_info, y="got_a_TV", bins=10, parallel=FALSE)
IV_value = data.frame(IV$Summary)
print(IV_value)
# amount_financing is strongest predictor
# amount_purchase, LT_clients, promotions_used, require_financing are medium predictors
Information::plot_infotables(IV, IV$Summary$Variable[1:23], same_scale=FALSE, show_values=TRUE)
