library('reshape')

# Faz a leitura do CSV fornecido pelo python
dir <- paste(dirname(sys.frame(1)$ofile), '/../datasets/issueTypesWorkload.csv', sep = '')
csv <- read.csv(dir)
cht <- melt(csv)

# Define os labels
lbs <- cht[, 1]
lbs <- paste(lbs, round(cht[, 2]/sum(cht[, 2])*100))
lbs <- paste(lbs,"%",sep="")

# Monta o gráfico
pie(cht[, 2], labels = lbs, main="Issue Types")