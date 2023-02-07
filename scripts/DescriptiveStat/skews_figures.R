library(ggplot2)
library(ggpubr)

cock_term_skew <- read.csv("/home/gab/Documents/lab/TermitesAndCockroaches/MutSpec-Redone/interim/DescriptiveStat/cock_term_skews.csv")
cock_term_skew$Gene_name <- factor(cock_term_skew$Gene_name, levels = c( "COX1", "COX2", "ATP8", "ATP6",  "COX3", "ND3", "ND4L", "ND4", "ND5", "CYTB"))

#74B72E - cock color, #466D1D -term color (didn't use)


######GA#########
cock_termGAskew <- ggplot(data=subset(cock_term_skew, !is.na(cock_term_skew$Gene_name)), aes(x=Gene_name, y=GAskew, fill=Organism)) + 
  geom_boxplot() + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))

cock_termGAskew


#######TC#######
cock_termTCskew <- ggplot(data=subset(cock_term_skew, !is.na(cock_term_skew$Gene_name)), aes(x=Gene_name, y=TCskew, fill=Organism)) + 
  geom_boxplot() + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                                      panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))

cock_termTCskew


#######Stg-Sac######
cock_term_StgSac_skew <- ggplot(data=subset(cock_term_skew, !is.na(cock_term_skew$Gene_name)), aes(x=Gene_name, y=Stg.Sac, fill=Organism)) + 
  geom_boxplot() + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                                      panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))

cock_term_StgSac_skew


#####GTassymetry####

# I merged them manually and also manually added organism names
gt_assymetry <- read.csv("/home/gab/Documents/lab/TermitesAndCockroaches/MutSpec-Redone/interim/DescriptiveStat/GTasymmetry_merged.csv")
g_assymetry <- ggplot(data=gt_assymetry, aes(x=organism, y=med_c)) + ylab("Median G") +
  geom_boxplot() + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                                      panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) 
g_assymetry

t_assymetry <- ggplot(data=gt_assymetry, aes(x=organism, y=med_a)) + ylab("Median T") +
  geom_boxplot() + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                                      panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) 
t_assymetry
