Title: RunDMC in a jupyter notebook
Date: 2021-10-18 9:12
Modified: 2021-10-18 9:12
Category: posts
Tags: resources, tutorial
Authors: Gabriel 
Summary: A brief tutorial on how to get the R packages runDMC in a jupyter environment through anaconda.

Sorry, it's not about how to invite runDMC rappers to feature your notebook, rather it is about using the package "dynamic models of choice" ([runDMC](https://osf.io/pbwx8/)), to fit decision making models to your behavioral (and physiological) data within the environment of Jupyter.

Why you ask ? Well, I'm allergic to development environment such as Rstudio or Rmarkdown as they are, to me, not practical enough when it comes to explore your data or your analysis pipeline while keeping a record of everythin. For that I prefer the jupyter environment but installing R and it's packages can be tricky, especially with complex architectures such as the one required by runDMC. Therefore I wrote this short tutorial in case others want to use the ability of jupyter but still rely on runDMC to do your decision data anaysis.

We we'll be using conda, if you do not arleady have anaconda installed download the latest version at [anaconda.com](https://docs.anaconda.com/anaconda/install/index.html).

First we will ensure that packages from conda are downloaded from the conda-forge repositories that has a larger collection of packages than default conda repositories. For that, in a terminal (for linux and Mac users) or using the anaconda prompt (for windows) launch the following command : 

    conda config --add channels conda-forge
    conda config --set channel_priority strict 

Then we will simultaneously create a new environment called "DMC" with the available and required packages from conda-forge : 

    conda create -n DMC r-loo r-hypergeo r-statmod r-pracma r-snowfall r-numDeriv r-vioplot r-ggplot2 r-gridExtra r-truncdist r-msm r-rlecuyer r-laplacesdemon r-mvtnorm r-matrix jupyter #That will take a while

However a few of the required packages are not contained in the conda forge rep (rtdists, stringr, Brobdingnag) . We therefore have to launch an R session in the DMC environment to install them afterwards. For that first launch an R session by previously activating our new conda env : 

    conda activate DMC
    R
    install.packages("Brobdingnag") # This will prompt a screen requiring to select a server from which you will download, just select the nearest one
    install.packages("stringr") 
    install.packages("rtdists") 

Then we will install a modified version of the coda package that allows for plotting of priors with plot.dmc.
For that download the zip file from the [latest DMC version](https://osf.io/njsqa/), extract it in a relevant path and then move to that working directory within the R session, in my case and for the version 190819 it goes as follows : 

    setwd("~/DMC_190819")
    
And install the coda package :

    install.packages("packages/coda_0.19-3.tar.gz",repos=NULL,type="source")

Then R and jupyter packages are not interfacing very well you need a last step to provide jupyter with the relevant locations for the R package : 

     install.packages('IRkernel') 
     IRkernel::installspec() 
     
Et voilà ! You're ready to go and use runDMC and the associated tutorials :)

Let me know in case you run into troubles.
