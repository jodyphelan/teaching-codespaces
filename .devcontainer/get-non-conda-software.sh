mkdir -p ~/git
cd ~/git
git clone https://github.com/jodyphelan/genomics_course.git

bash ~/git/genomics_course/scripts/setup_machine/03_get_non_conda_programs.sh

mkdir -p ~/.firefox
echo "user_pref(\"webgl.force-enabled\", true);" > ~/.firefox/user.js
# make alias
echo 'alias "firefox=firefox --profile ~/.firefox/"' >> ~/.bashrc