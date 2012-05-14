#ifndef IPTRAF_NG_COMPAT_H
#define IPTRAF_NG_COMPAT_H

#include <stdlib.h>
#include <unistd.h>
#include <getopt.h>
#include <signal.h>
#include <string.h>
#include <time.h>
#include <fcntl.h>
#include <dirent.h>
#include <errno.h>
#include <ctype.h>
#include <netdb.h>
#include <curses.h>
#include <panel.h>
#include <assert.h>
#include <stddef.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <sys/time.h>
#include <sys/ioctl.h>
#include <sys/wait.h>
#include <sys/un.h>

#include <netinet/in.h>
#include <netinet/udp.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <netinet/ip6.h>
#include <netinet/icmp6.h>
#include <netinet/ip_icmp.h>

#include <arpa/inet.h>

#include <linux/if_ether.h>
#include <linux/if_packet.h>
#include <linux/if_fddi.h>
#include <linux/if_tr.h>
#include <linux/types.h>
#include <linux/isdn.h>

#include <linux/if.h>
#include <linux/if_arp.h>

/* move it out! */
#include "tui/labels.h"
#include "tui/listbox.h"
#include "tui/input.h"
#include "tui/menurt.h"
#include "tui/winops.h"
#include "tui/msgboxes.h"
//#include "txbox.h"

#define debug(...)							\
	do {								\
                fprintf(stderr, "%s:%s():%d:",				\
			__FILE__, __func__, __LINE__);			\
                fprintf(stderr, __VA_ARGS__);				\
                fprintf(stderr, "\n");					\
	} while(0)

#define KBITS 0

#define dispmode(mode)				\
	(((mode) == KBITS) ? "kbps": "kBps")

#define __noreturn __attribute__((noreturn))
#define __unused __attribute__((unused))


#define alloc_nr(x) (((x)+16)*3/2)

/*
 * Realloc the buffer pointed at by variable 'x' so that it can hold
 * at least 'nr' entries; the number of entries currently allocated
 * is 'alloc', using the standard growing factor alloc_nr() macro.
 *
 * DO NOT USE any expression with side-effect for 'x', 'nr', or 'alloc'.
 */
#define ALLOC_GROW(x, nr, alloc)					\
	do {								\
		if ((nr) > alloc) {					\
			if (alloc_nr(alloc) < (nr))			\
				alloc = (nr);				\
			else						\
				alloc = alloc_nr(alloc);		\
			x = xrealloc((x), alloc * sizeof(*(x)));	\
		}							\
	} while (0)


extern void *xmalloc(size_t size);
extern void *xcalloc(size_t nmemb, size_t size);
extern void *xrealloc(void *ptr, size_t size);
extern void *xmallocz(size_t size);
extern char *xstrdup(const char *s);
extern int strtoul_ui(char const *s, int base, unsigned int *result);
extern int strtol_i(char const *s, int base, int *result);

extern void die(const char *err, ...);
extern void die_errno(const char *err) __noreturn;
extern void error(const char *err, ...);

static inline char *skip_whitespace(char *str)
{
	while (isspace(*str))
		++str;

	return str;
}

#endif	/* IPTRAF_NG_COMPAT_H */
