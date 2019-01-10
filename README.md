# cplex_tramp_steamer

To run at Intel:
````
source ~/ppt_work_area/general/bin/activate.csh

python gen_lp.py > foo.lp

/nfs/site/proj/dt/pdx_sde02/x86-64_linux26/cplex/12.2/cplex/bin/x86_sles10_4.1/cplex << EOF
read foo.lp
netopt
EOF
````
