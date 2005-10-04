if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
map! <S-Insert> <MiddleMouse>
map! <xHome> <Home>
map! <xEnd> <End>
map! <S-xF4> <S-F4>
map! <S-xF3> <S-F3>
map! <S-xF2> <S-F2>
map! <S-xF1> <S-F1>
map! <xF4> <F4>
map! <xF3> <F3>
map! <xF2> <F2>
map! <xF1> <F1>
vmap ,, :call Async_event("switchfocus,")
vmap ,m :call Async_event("pastebin,".@")
vmap ,? :call Async_event("doc,".@")
vmap ,/ :call Async_event("doc,".expand('<cword>'))
vmap ,B :call Async_event("breakpointclear,".line("."))
vmap ,b :call Async_event("breakpointset,".line("."))
vmap ,p :call Async_event("projectexecute,")
vmap ,x :call Async_event("bufferexecute,")
nmap ,, :call Async_event("switchfocus,")
nmap ,m :call Async_event("pastebin,".@")
nmap ,? :call Async_event("doc,".@")
nmap ,/ :call Async_event("doc,".expand('<cword>'))
nmap ,B :call Async_event("breakpointclear,".line("."))
nmap ,b :call Async_event("breakpointset,".line("."))
nmap ,p :call Async_event("projectexecute,")
nmap ,x :call Async_event("bufferexecute,")
nmap \sv <Plug>SVNVimDiff
nmap \su <Plug>SVNUpdate
nmap \si <Plug>SVNInfo
nmap \ss <Plug>SVNStatus
nmap \sr <Plug>SVNReview
nmap \sq <Plug>SVNRevert
nmap \sl <Plug>SVNLog
nmap \sd <Plug>SVNDiff
nmap \sc <Plug>SVNCommit
nmap \sn <Plug>SVNAnnotate
nmap \sa <Plug>SVNAdd
vnoremap p :let current_reg = @"gvdi=current_reg
map <S-Insert> <MiddleMouse>
nnoremap <Plug>SVNVimDiff :SVNVimDiff
nnoremap <Plug>SVNUpdate :SVNUpdate
nnoremap <Plug>SVNInfo :SVNInfo
nnoremap <Plug>SVNStatus :SVNStatus
nnoremap <Plug>SVNReview :SVNReview
nnoremap <Plug>SVNRevert :SVNRevert
nnoremap <Plug>SVNLog :SVNLog
nnoremap <Plug>SVNDiff :SVNDiff
nnoremap <Plug>SVNCommit :SVNCommit
nnoremap <Plug>SVNAnnotate :SVNAnnotate
nnoremap <Plug>SVNAdd :SVNAdd
map <xHome> <Home>
map <xEnd> <End>
map <S-xF4> <S-F4>
map <S-xF3> <S-F3>
map <S-xF2> <S-F2>
map <S-xF1> <S-F1>
map <xF4> <F4>
map <xF3> <F3>
map <xF2> <F2>
map <xF1> <F1>
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
set autowrite
set backspace=indent,eol,start
set expandtab
set fileencodings=ucs-bom,utf-8,latin1
set helplang=pt
set history=50
set hlsearch
set ignorecase
set incsearch
set mouse=a
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,/etc/vim,/usr/share/vim/vimfiles,/usr/share/vim/addons,/usr/share/vim/vim63,/usr/share/vim/vimfiles,/usr/share/vim/addons/after,~/.vim/after
set shiftround
set shiftwidth=4
set showbreak=<
set showcmd
set showmatch
set smarttab
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set tabstop=4
set termencoding=utf-8
set viminfo='20,\"50
set wildignore=*.pyc
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Novidades
set shortmess=aoO
badd +90 ~/projetos/handtalks-pc/JanelaPrincipal.py
badd +1 ~/projetos/handtalks-pc/tocador.py
silent! argdel *
edit ~/projetos/handtalks-pc/JanelaPrincipal.py
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
exe '1resize ' . ((&lines * 41 + 26) / 52)
exe '2resize ' . ((&lines * 8 + 26) / 52)
argglobal
setlocal noarabic
setlocal autoindent
setlocal autoread
setlocal nobinary
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:XCOMM,n:>,fb:-
setlocal commentstring=#%s
setlocal complete=.,w,b,u,t,i
setlocal nocopyindent
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatoptions=tcq
setlocal grepprg=
setlocal iminsert=2
setlocal imsearch=2
setlocal include=s*\\(from\\|import\\)
setlocal includeexpr=substitute(v:fname,'\\.','/','g')
setlocal indentexpr=
setlocal indentkeys=0{,0},:,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keymap=
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=octal,hex
setlocal nonumber
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal noreadonly
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal nosmartindent
setlocal softtabstop=0
setlocal suffixesadd=.py
setlocal swapfile
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tags=
setlocal textwidth=0
setlocal thesaurus=
setlocal nowinfixheight
setlocal wrap
setlocal wrapmargin=0
silent! normal! zE
let s:l = 99 - ((26 * winheight(0) + 20) / 41)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
99
normal! 025l
wincmd w
argglobal
enew
setlocal noarabic
setlocal autoindent
setlocal autoread
setlocal nobinary
setlocal bufhidden=delete
setlocal buflisted
setlocal buftype=quickfix
setlocal nocindent
setlocal cinkeys=0{,0},0),:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal nocopyindent
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'qf'
setlocal filetype=qf
endif
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatoptions=tcq
setlocal grepprg=
setlocal iminsert=2
setlocal imsearch=2
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keymap=
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal nomodifiable
setlocal nrformats=octal,hex
setlocal nonumber
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal noreadonly
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal nosmartindent
setlocal softtabstop=0
setlocal suffixesadd=
setlocal noswapfile
if &syntax != 'qf'
setlocal syntax=qf
endif
setlocal tabstop=4
setlocal tags=
setlocal textwidth=0
setlocal thesaurus=
setlocal winfixheight
setlocal wrap
setlocal wrapmargin=0
wincmd w
exe '1resize ' . ((&lines * 41 + 26) / 52)
exe '2resize ' . ((&lines * 8 + 26) / 52)
set winheight=1 winwidth=20 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . s:sx
endif
let &so = s:so_save | let &siso = s:siso_save
