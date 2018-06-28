library("openair", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.4")


args <- commandArgs(trailingOnly = TRUE)

rocne_bunky  <- read.csv(file.path("/data","rio",paste(args[1], sep = ""), paste(args[1], "_ann_cell.csv", sep = "")), header = TRUE)
summary(rocne_bunky)
modStats(rocne_bunky, obs = "rio", mod = "cmaq")

write.csv(modStats(rocne_bunky, obs = "rio", mod = "cmaq"), file=file.path("/data","rio",paste(args[1], sep = ""),"statistics", paste(args[1], "_cell_annual_stat.csv", sep = "")))

png(filename=file.path("/data","rio",paste(args[1], sep = ""),"statistics",paste(args[1], "_cell_annual_Taylor.png", sep = "")),
    units="in",
    width=5,
    height=4,
    pointsize=12,
    res=400)
TaylorDiagram(rocne_bunky, obs = "rio", mod = "cmaq")
dev.off()


denne_bunky  <- read.csv(file.path("/data","rio",paste(args[1], sep = ""), paste(args[1], "_day_cell.csv", sep = "")), header = TRUE)
denne_bunky$date <- as.POSIXct(strptime(denne_bunky$date, format = "%Y-%m-%d", tz = "GMT"))
modStats(denne_bunky, obs = "rio", mod = "cmaq")

write.csv(modStats(denne_bunky, obs = "rio", mod = "cmaq"), file=file.path("/data","rio",paste(args[1], sep = ""),"statistics", paste(args[1], "_cell_daily_stat.csv", sep = "")))

png(filename=file.path("/data","rio",paste(args[1], sep = ""),"statistics",paste(args[1],"_cell_daily_Taylor.png", sep = "")),
    units="in",
    width=5,
    height=4,
    pointsize=12,
    res=400)
TaylorDiagram(denne_bunky, obs = "rio", mod = "cmaq")
dev.off()


denne_bunky_st  <- read.csv(file.path("/data","rio",paste(args[1], sep = ""), paste("stations_", args[1], "_daily.csv", sep = "")), header = TRUE)
denne_bunky_st$date <- as.POSIXct(strptime(denne_bunky_st$date, format = "%Y-%m-%d", tz = "GMT"))
modStats(denne_bunky_st, obs = "obser", mod = "mod",type="group")
modStats(denne_bunky_st, obs = "obser", mod = "mod",type=c("group","country"))
modStats(denne_bunky_st, obs = "obser", mod = "mod",type=c("group","season"))

write.csv(modStats(denne_bunky_st, obs = "obser", mod = "mod",type="group"), file=file.path("/data","rio",paste(args[1], sep = ""),"statistics", paste(args[1], "_stations_daily_stat.csv", sep = "")))

png(filename=file.path("/data","rio",paste(args[1], sep = ""),"statistics",paste(args[1], "_stations_daily_Taylor.png", sep = "")),
    units="in",
    width=5,
    height=4,
    pointsize=12,
    res=400)
TaylorDiagram(denne_bunky_st, obs = "obser", mod = "mod", group = "group")
dev.off()























