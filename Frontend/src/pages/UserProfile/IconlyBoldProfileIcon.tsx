import { memo, SVGProps } from "react";

const IconlyBoldProfileIcon = (props: SVGProps<SVGSVGElement>) => (
  <svg
    preserveAspectRatio="none"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    {...props}
  >
    <path
      fillRule="evenodd"
      clipRule="evenodd"
      d="M17.2539 7.40036C17.2539 10.3829 14.9028 12.8007 12.0026 12.8007C9.10241 12.8007 6.75131 10.3829 6.75131 7.40036C6.75131 4.41782 9.10241 2 12.0026 2C14.9028 2 17.2539 4.41782 17.2539 7.40036ZM16.5099 15.8434C18.1796 16.1815 19.2697 16.7331 19.7369 17.6228C20.0877 18.3171 20.0877 19.1437 19.7369 19.8381C19.2697 20.7278 18.2229 21.3149 16.4926 21.6174C15.7216 21.7729 14.9412 21.874 14.1568 21.9199C13.4301 22 12.7034 22 11.968 22H10.6444C10.3675 21.9644 10.0994 21.9466 9.83981 21.9466C9.05538 21.9063 8.27477 21.8082 7.50397 21.653C5.83428 21.3327 4.74422 20.7633 4.27706 19.8737C4.09671 19.529 4.00163 19.144 4.00022 18.7527C3.99646 18.3589 4.08866 17.9705 4.2684 17.6228C4.72692 16.7331 5.81698 16.1548 7.50397 15.8434C8.27816 15.6915 9.06144 15.5934 9.84846 15.5498C11.2881 15.4338 12.7344 15.4338 14.1741 15.5498C14.9581 15.5955 15.7383 15.6936 16.5099 15.8434Z"
      fill="black"
    />
  </svg>
);
const Memo = memo(IconlyBoldProfileIcon);
export { Memo as IconlyBoldProfileIcon };
