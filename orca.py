ó
·>ãZc           @   så  d  Z  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 m Z m Z d d l m Z d d l m Z d e f d     YZ d e f d	     YZ d
 e f d     YZ d e f d     YZ d d d     YZ d e f d     YZ d e f d     YZ d e f d     YZ e d k ráe e j  d k r¡e j d d k r­e d e  j Z q­n e   j Z e j d j  e    e   e   e   j!   n  d S(   s   1.4iÿÿÿÿN(   t   AzureExceptiont   AzureMissingResourceHttpError(   t   urljoin(   t   FileServicet   Statec           B   s   e  Z e Z d  Z RS(   i    (   t   __name__t
   __module__t   Falset   ERRORt   ERROR_COUNT(    (    (    s   orca.pyR   8   s   t   Configc           B   sb   e  Z d Z d Z d Z d  Z d Z d Z d Z	 d Z
 d Z d Z d Z d Z d Z d Z d Z RS(   i    N(   R   R   t   Nonet
   SERIAL_NUMt   POLLING_INTERVALt   RETRY_INTERVALt   START_DELAYt
   MAX_ERRORSt
   IP_ADDRESSt   LOG_DIRECTORYt   LOG_FILEt   MAX_RECORDSt   LOGINt   PASSWORDt   ACCOUNTt   KEYt   SHAREt   UPLOADED_FILE(    (    (    s   orca.pyR
   >   s   t	   GetConfigc           B   s   e  Z d  Z d   Z RS(   s   /home/pi/orca/orca.confc         C   s0  yÙt  j    |  _ |  j j |  j  |  j j d d  t _ |  j j d d  d t _ |  j j d d  d t _	 |  j j d d  d t _
 |  j j d d  t _ |  j j d d	  t _ |  j j d d
  t _ t j j d  sý t j d 7_ n  |  j j d d  t _ |  j j d d  t _ |  j j d d  t _ |  j j d d  t _ |  j j d d  t _ |  j j d d  t _ |  j j d d  t _ |  j j d d  t _ t j j d t j  t _ WnP t k
 r+} t j d j |  j   t j |  t j d  t d  n Xd  S(   Nt   Generalt   UnitSerialNumbert   PollingIntervali`ê  t   RetryIntervalt
   StartDelayt	   MaxErrorst   HMIt	   IPAddresst   LogDirectoryt   /t   LogFilet
   MaxRecordst   Logint   Passwordt   Azuret   Accountt   Keyt   Sharet   UploadedFiles   {UnitSerialNumber}s+   Missing or malformed {} configuration file!s	   Exiting.
i   (   t   ConfigParsert   settingst   readt   CONFIG_FILEt   getR
   R   t   getintR   R   R   R   R   R   t   endswithR   R   R   R   R   R   R   R   t   replacet	   Exceptiont   logt   criticalt   formatt   debugt   infot   exit(   t   selft   e(    (    s   orca.pyt   __init__T   s>    	(   R   R   R2   R@   (    (    (    s   orca.pyR   R   s   t   CheckDiskSpacec           B   s   e  Z d    Z RS(   c         C   s½   t  j d  t j d  } | j | j } | j | j } t t | |  t |  d  } t  j d j	 |   | d k r¹ t  j d  t j
 d  t  j d  t j
 d	  n  d  S(
   Ns   Checking disk space...R%   id   s   Disk utilization {0}%.iK   s!   Cleaning up /var/log directory...s   sudo rm -f /var/log/*s!   Rebooting system after cleanup...s   sudo reboot(   R8   R<   t   ost   statvfst   f_blockst   f_frsizet   f_bavailt   intt   floatR:   t   system(   R>   t   statst   totalt   freet   disk_usage_percent(    (    s   orca.pyR@   x   s    $(   R   R   R@   (    (    (    s   orca.pyRA   w   s   t   Loggerc           B   s   e  Z e d   Z d   Z RS(   c         C   s  d } d } d } d } t  j j |  s: t  j |  n  t j d  } t j d d d } t j   } | j |  | j t j	  t j
 j d	 j | |  d
 | d | }	 |	 j |  |	 j t j	  t j
 j d j | |  d
 | d | }
 |
 j |  |
 j t j  t j |  |  _ |  j j t j  |  j j |	  |  j j |
  | rs|  j j |  n  |  j t _ d  S(   NiPÃ  i
   s   /home/pi/orca/log/t   orcas   %(message)ss4   %(asctime)s [%(process)d] %(levelname)s: %(message)st   datefmts   %Y-%m-%d %H:%M:%Ss
   {0}{1}.logt   maxBytest   backupCounts   {0}{1}.errors.log(   RB   t   patht   existst   makedirst   loggingt	   Formattert   StreamHandlert   setFormattert   setLevelt   INFOt   handlerst   RotatingFileHandlerR:   R   t	   getLoggerR8   t   DEBUGt
   addHandlert   handle_exceptiont   syst
   excepthook(   R>   t   log_to_consolet	   MAX_BYTESt   BACKUP_COUNTt   LOG_PATHt   LOG_NAMEt   console_fmtt   file_fmtt   console_handlert   file_handlert   error_file_handler(    (    s   orca.pyR@      s@    					 c         C   s|   | t  j k r[ |  j j d d | | | f |  j j d  t j d  t j d  n |  j j d  t j d  d  S(   Ns   *** UNCAUGHT EXCEPTION ***t   exc_infos   *** REBOOTING SYSTEM NOW ***s   sudo rebooti
   s   Keyboard interrupt.i   (	   t
   exceptionst   KeyboardInterruptR8   t   errorRB   RI   Rb   R=   R<   (   R>   t   excTypet   excValuet	   traceback(    (    s   orca.pyRa   º   s    (   R   R   R   R@   Ra   (    (    (    s   orca.pyRN      s   0R"   c           B   s   e  Z d    Z RS(   c         C   s°  d } d } d } i t  j d 6t  j d 6} t j   r} t j d j | t  j   yé| j	 t
 d j | t  j  |  d | d	 d
 } t
 d j | t  j  t  j  } t
 | t  j  } t j d j |   d } | j | d	 d
 d t }	 t | d  M }
 xC |	 j d d  D]/ } | r| | j d  7} |
 j |  qqWWd  QXt | d  Ù }
 |
 j   }	 d |	 j   k sd |	 j   k ròt j d  d |	 j   k rÆt j d  n t j d j t  j t  j   t t _ t Sx% t | t  j  D] } |
 j   qWx |
 D] } |	 | 7}	 q!W|	 SWd  QXWnc t j j k
 r~} t j d j t  j   t t _ t St k
 r¥t j d  t t _ t SXWd  QXd  S(   Ns   /tmp/temp.dats   http://t	   FormLoginR(   R)   s   Connecting to {}{}s   {}{}t   datat   timeouti
   s   Fetching {}iÿÿÿÿt   streamt   wt
   chunk_sizei   s   
t   rs   <HTML>s   !DOCTYPEs"   HMI Error: Could not retrieve CSV.s7   SERVER GIVES NO SPECIFIC INFORMATION TO THIS ERROR CODEs<   Got: Server gives no specific Information to this Error codes)   Check authentication credentials: {0}/{1}s   Network {} is unreachable.
s   Out of memory!(   R
   R   R   t   requestst   SessionR8   R<   R:   R   t   postR   R   R   R3   t   Truet   opent   iter_contentt   countt   writet   readlinet   upperRq   R   R   R   t   xrangeR   Ro   t   ConnectionErrort   MemoryError(   R>   t	   temp_filet   prefixt	   auth_paget   auth_payloadt   st   pt   urlt
   line_countR{   t   ft   chunkt   xt   lineR?   (    (    s   orca.pyt   get_CSV_from_web_interfaceÉ   sb    
		$			(   R   R   R   (    (    (    s   orca.pyR"   È   s   R*   c           B   s   e  Z d    Z RS(   c         C   s;  d } t  j   ? } y | j | d d Wn t j d  t t _ t SXWd  QXt	 d t
 j d t
 j  } yL t j d j t
 j t
 j   | j t
 j d  t
 j |  t j d  Wnz t k
 ræ } t j d	  t t _ d  St k
 r} t j d
  t t _ d  St k
 r6t j d  t t _ d  SXd  S(   Ns   http://www.google.comRw   i
   s   Error: Internet is unreachable.t   account_namet   account_keys   Uploading {} to Azure share \{}s   Done.s;   Azure Connection Error: The specified share does not exist.s9   Azure Connection Error: Bad key or service not available.s   Out of memory!(   R|   R}   R3   R8   Rq   R   R   R   R   R   R
   R   R   R<   R:   R   R   t   create_file_from_textR   R   R    R   (   R>   Rv   t   hostR   t   azure_file_serviceR?   (    (    s   orca.pyt   upload  s<    				(   R   R   R   (    (    (    s   orca.pyR*     s   t   Mainc           B   s,   e  Z d    Z d   Z d   Z d   Z RS(   c         C   s2   t    |  _  t   |  _ t j t j |  j  d  S(   N(   R"   R*   t   signalt   SIGTERMt   SIGTERM_handler(   R>   (    (    s   orca.pyR@   <  s    c         C   s   t  j d  t d  d  S(   Ns.   **** GOT KILL SIGNAL - PROGRAM TERMINATED ****iÿÿÿÿ(   R8   R9   R=   (   R>   t   signumt   frame(    (    s   orca.pyR   A  s    c         C   s   t  j d k r/ t j d j t  j d   n  t j t  j |  j  z9 y t j   j	   Wn t
 k
 r| t j d  n XWd  t j   j   Xd  S(   Ni    s   Delaying {} minute(s)...i`ê  s   Keyboard interrupt.(   R
   R   R8   R<   R:   t   gobjectt   timeout_addt   get_CSVt   MainLoopt   runRp   t   quit(   R>   (    (    s   orca.pyR¦   E  s      c         C   s  t  t _ |  j j   |  _ |  j r: |  j j |  j  n  t j rÐ t j	 r t j
 d 7_
 t j
 t j	 k r t j d  t j d  t j d  q n  t j d j t j d   t j t j |  j  n< d t _
 t j d j t j d   t j t j |  j  d  S(   Ni   s4   Maximum error count exceeded.  Rebooting system now.s   sudo reboots!   Next attempt in {0} minute(s)...
i`ê  i    (   R   R   R   R"   R   t   ORCA_logR*   R   R
   R   R	   R8   R9   RB   RI   Rb   R=   R<   R:   R   R¢   R£   R¤   R   (   R>   (    (    s   orca.pyR¤   P  s     					(   R   R   R@   R   R¦   R¤   (    (    (    s   orca.pyR   ;  s   			t   __main__i   s   -vRd   s$   

**** PROGRAM START (VER {0}) ****
(    ("   t   VERSIONRB   Rb   R   R¢   RV   t   logging.handlersR|   Ro   R/   t   azure.commonR    R   t   urlparseR   t   azure.storage.fileR   t   objectR   R
   R   RA   RN   R"   R*   R   R   t   lent   argvR   R8   R<   R:   R¦   (    (    (    s   orca.pyt   <module>'   s:   %?J)3