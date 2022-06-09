cd /home/cxxu/backEnd/
# ls
# git checkout main
git reset --hard origin/main
git log|head -n 10
# git pull origin main
git status |head -n 10
echo `date`
echo '----brute force pull done!(by reset --hard to the remote origin/main---)'