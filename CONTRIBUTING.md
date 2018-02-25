#Contibuting to AdperSense

## Welcome contributors to the project: 

## How to submit changes: Pull Request protocol etc. 
**1**. _**Fork**_ the repository

**2**. Clone the _original repository_ to your local PC using one of the following commands based on the protocol you are using:
 * HTTPS:`git clone https://github.com/campbell-joshua/AdperSense.git --origin upstream --recursive`
 * SSH:`git clone git@github.com:campbell-joshua/AdperSense.git --origin upstream --recursive`
 * Then rebase: `git rebase upstream master`
 If you use HTTPS, you will have to log in each time when pushing to your fork. (Recommended: learn about git SSH support, it logs in automatically using SSH keys)
 
**3**. **Add** your fork with
 * HTTPS:`git remote add origin https://github.com/your-username/AdperSense.git
 * SSH:`git remote add origin git@github.com:your-username/AdperSense.git
 
**4**. Alternatively, if you already have a fork and copy of the repo, you can simply check to **make sure you're up-to-date**
 * Pull the upstream:`git pull upstream --rebase`
 * Update the submodules:`git submodule update --recursive --init`
 
**5**. Create a _**separate branch**_ (recommended if you're making multiple changes simultaneously) (`git checkout -b my-branch`)

**6**. _Make changes_

**7**. **Commit** (`git add <item(s) you changed>; git commit`) and write your commit message

**8**. Test your changes by **cleaning** (`make clean; git clean -Xfd`)`.

**9**. _**Pull**_ from upstream (`git pull upstream --rebase`) (Note: Make sure to include `--rebase`, as it will apply your changes on top of the changes you just pulled, allowing for a much cleaner merge)

**10**. Push to **your fork** (`git push origin <branch>`), `<branch>` being the branch you created earlier

**11**. Create a _pull request_

**12**. If your changes are _minor_, you can just describe them in a paragraph or less. If they're _major_, please fill out the provided form.

**13. Submit!**   

## How to report a bug: 
Open an issue on the repo
 
