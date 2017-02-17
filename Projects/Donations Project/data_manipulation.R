main_df <- read.csv('donation_data_clean.csv')

main_df$avgCON <- main_df$CNTRLIF/main_df$CNTMLIF

month <- main_df$CNDAT1 %% 12

for (i in 1:length(month)) {
  if (month[i] == 0 || month[i] == 1) {
    main_df$month1[i] <- 1
  } else if (month[i] == 2 || month[i] == 3) {
    main_df$month1[i] <- 2
  } else if (month[i] == 4 || month[i] == 5) {
    main_df$month1[i] <- 3
  } else if (month[i] == 6 || month[i] == 7) {
    main_df$month1[i] <- 4
  } else if (month[i] == 8 || month[i] == 9) {
    main_df$month1[i] <- 5
  } else if (month[i] == 10 || month[i] == 11) {
    main_df$month1[i] <- 6
  } 
}

for (i in 1:length(month)) {
  if (month[i] == 0) {
    main_df$month2[i] <- 1
  } else if (month[i] == 1) {
    main_df$month2[i] <- 2
  } else if (month[i] == 2) {
    main_df$month2[i] <- 3
  } else if (month[i] == 3) {
    main_df$month2[i] <- 4
  } else if (month[i] == 4) {
    main_df$month2[i] <- 5
  } else if (month[i] == 5) {
    main_df$month2[i] <- 6
  } else if (month[i] == 6) {
    main_df$month2[i] <- 7
  } else if (month[i] == 7) {
    main_df$month2[i] <- 8
  } else if (month[i] == 8) {
    main_df$month2[i] <- 9
  } else if (month[i] == 9) {
    main_df$month2[i] <- 10
  } else if (month[i] == 10) {
    main_df$month2[i] <- 11
  } else if (month[i] == 11) {
    main_df$month2[i] <- 12
  } 
}
str(main_df)

main_df$month1 <- as.factor(main_df$month1)
main_df$month2 <- as.factor(main_df$month2)





### new stuff

# adding big donor state one

don_state <- c('WY', 'WI', 'SD', 'PA', 'PR', 'OH', 'ND', 'MN', 'IN', 'IA', 
               'GU', 'AK' , 'NY', 'NJ', 'NE', 'MO', 'MI', 'MA', 'CT', 'AZ')

main_df$don_state <- ifelse(main_df$STATCODE %in% don_state, 1, 0)

# doing outlier removal



main_df2 <- main_df[which(main_df$TARGDOL != 1500),]
main_df2 <- main_df2[which(main_df2$CNTRLIF < 3000),]
main_df2 <- main_df2[which(main_df2$CNDOL1 < 220),]
main_df2 <- main_df2[which(main_df2$CONTRFST < 4000),]
main_df2 <- main_df2[which(main_df2$CONLARG < 400),]
main_df2 <- main_df2[which(main_df2$CNMON1 < 120),]

  
write.csv(main_df2, 'data_clean_manip.csv')


