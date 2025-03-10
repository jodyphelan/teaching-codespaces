mkdir -p ~/git
cd ~/git
git clone https://github.com/jodyphelan/genomics_course.git

bash ~/git/genomics_course/scripts/setup_machine/03_get_non_conda_programs.sh


ln -s ~/miniforge3/condabin/mamba ~/bin/mamba

echo 'alias "ca=conda activate"' >> ~/.bashrc
